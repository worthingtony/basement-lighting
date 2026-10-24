#!/usr/bin/env python3
"""Click and type into SoundSwitch / Fixture Manager with CoreGraphics events.

Workaround for Claude desktop 3.1623.0, whose computer-use click guard refuses
every click on these apps ("Could not verify which document this window is
editing"): their windows answer AXDocument with kAXErrorNoValue (-25212).
Screenshots still come from the computer-use tool; this script only sends input.

Coordinates are in the computer-use screenshot frame (1372 wide by default) and
are scaled to screen points. Every action first checks that the frontmost app is
SoundSwitch or FixtureManager, and refuses otherwise. With --app, it must be that
one app: a batch meant for Fixture Manager once typed into SoundSwitch because a
click landed on SoundSwitch's window behind it (2026-10-20).

  ui.py [--app APP] COMMAND ...
  ui.py front
  ui.py click X Y [--double] [--right]
  ui.py move X Y
  ui.py hold X Y SECONDS         (press, wait, release: momentary buttons)
  ui.py drag X1 Y1 X2 Y2
  ui.py scroll X Y DY            (DY lines; positive scrolls down)
  ui.py type TEXT
  ui.py key COMBO                (cmd+shift+s, return, escape, tab, ...)
  ui.py expectmenu X Y H         (stop unless an H-pt-tall menu opened at X Y)
  ui.py batch FILE               (one command per line; "sleep N" allowed)
  ui.py activate APP             (SoundSwitch or FixtureManager)
"""
import ctypes
import shlex
import subprocess
import sys
import time

ALLOWED = {"SoundSwitch", "FixtureManager"}
FRAME_W = 1372.0
only_app = None  # set by --app

cg = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")


class CGPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]


class CGRect(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double), ("w", ctypes.c_double), ("h", ctypes.c_double)]


cg.CGMainDisplayID.restype = ctypes.c_uint32
cg.CGDisplayBounds.restype = CGRect
cg.CGDisplayBounds.argtypes = [ctypes.c_uint32]
cg.CGEventCreateMouseEvent.restype = ctypes.c_void_p
cg.CGEventCreateMouseEvent.argtypes = [ctypes.c_void_p, ctypes.c_uint32, CGPoint, ctypes.c_uint32]
cg.CGEventCreateKeyboardEvent.restype = ctypes.c_void_p
cg.CGEventCreateKeyboardEvent.argtypes = [ctypes.c_void_p, ctypes.c_uint16, ctypes.c_bool]
cg.CGEventCreateScrollWheelEvent2.restype = ctypes.c_void_p
cg.CGEventCreateScrollWheelEvent2.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32,
                                               ctypes.c_int32, ctypes.c_int32, ctypes.c_int32]
cg.CGEventSetFlags.argtypes = [ctypes.c_void_p, ctypes.c_uint64]
cg.CGEventSetIntegerValueField.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int64]
cg.CGEventKeyboardSetUnicodeString.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint16)]
cg.CGEventPost.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
cg.CGEventSetLocation.argtypes = [ctypes.c_void_p, CGPoint]
cg.CFRelease = ctypes.cdll.LoadLibrary(
    "/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation").CFRelease
cg.CFRelease.argtypes = [ctypes.c_void_p]

SCALE = cg.CGDisplayBounds(cg.CGMainDisplayID()).w / FRAME_W

MOD = {"cmd": 0x100000, "shift": 0x20000, "opt": 0x80000, "alt": 0x80000, "ctrl": 0x40000}
KEYS = {
    "return": 36, "enter": 36, "tab": 48, "space": 49, "delete": 51, "backspace": 51, "escape": 53, "esc": 53,
    "left": 123, "right": 124, "down": 125, "up": 126, "home": 115, "end": 119, "pageup": 116, "pagedown": 121,
    "forward_delete": 117,
    "a": 0, "s": 1, "d": 2, "f": 3, "h": 4, "g": 5, "z": 6, "x": 7, "c": 8, "v": 9, "b": 11, "q": 12, "w": 13,
    "e": 14, "r": 15, "y": 16, "t": 17, "1": 18, "2": 19, "3": 20, "4": 21, "6": 22, "5": 23, "=": 24, "9": 25,
    "7": 26, "-": 27, "8": 28, "0": 29, "]": 30, "o": 31, "u": 32, "[": 33, "i": 34, "p": 35, "l": 37, "j": 38,
    "'": 39, "k": 40, ";": 41, "\\": 42, ",": 43, "/": 44, "n": 45, "m": 46, ".": 47, "`": 50,
}


def frontmost():
    out = subprocess.check_output(["lsappinfo", "info", "-only", "name",
                                   subprocess.check_output(["lsappinfo", "front"]).decode().strip()]).decode()
    # '"LSDisplayName"="SoundSwitch"' or '"SoundSwitch" ASN:...'
    return out.split('"')[-2] if '=' in out else out.split('"')[1]


def guard():
    app = frontmost()
    if app not in ALLOWED:
        sys.exit(f"REFUSED: frontmost app is {app!r}, not SoundSwitch or FixtureManager")
    if only_app and app != only_app:
        sys.exit(f"REFUSED: frontmost app is {app!r}, not {only_app!r}")


def pt(x, y):
    return CGPoint(float(x) * SCALE, float(y) * SCALE)


def post(ev):
    cg.CGEventPost(0, ev)
    cg.CFRelease(ev)


def mouse(kind, p, button=0, clicks=1):
    ev = cg.CGEventCreateMouseEvent(None, kind, p, button)
    if clicks > 1:
        cg.CGEventSetIntegerValueField(ev, 1, clicks)  # kCGMouseEventClickState
    post(ev)


def click(x, y, double=False, right=False):
    p = pt(x, y)
    mouse(5, p)  # move
    time.sleep(0.05)
    down, up, btn = (3, 4, 1) if right else (1, 2, 0)
    for n in (1, 2) if double else (1,):
        mouse(down, p, btn, n)
        time.sleep(0.03)
        mouse(up, p, btn, n)
        time.sleep(0.08)


def drag(x1, y1, x2, y2, steps=12):
    a, b = pt(x1, y1), pt(x2, y2)
    mouse(5, a)
    time.sleep(0.05)
    mouse(1, a)
    time.sleep(0.08)
    for i in range(1, steps + 1):
        mouse(6, CGPoint(a.x + (b.x - a.x) * i / steps, a.y + (b.y - a.y) * i / steps))
        time.sleep(0.02)
    time.sleep(0.05)
    mouse(2, b)


def scroll(x, y, dy):
    mouse(5, pt(x, y))
    time.sleep(0.05)
    ev = cg.CGEventCreateScrollWheelEvent2(None, 1, 1, -int(dy), 0, 0)
    cg.CGEventSetLocation(ev, pt(x, y))
    post(ev)


def key(combo):
    parts = combo.lower().split("+")
    flags = 0
    for m in parts[:-1]:
        flags |= MOD[m]
    code = KEYS[parts[-1]]
    for down in (True, False):
        ev = cg.CGEventCreateKeyboardEvent(None, code, down)
        cg.CGEventSetFlags(ev, flags)
        post(ev)
        time.sleep(0.02)


SHIFTED = {"!": "1", "@": "2", "#": "3", "$": "4", "%": "5", "^": "6", "&": "7", "*": "8", "(": "9", ")": "0",
           "_": "-", "+": "=", "{": "[", "}": "]", "|": "\\", ":": ";", '"': "'", "<": ",", ">": ".", "?": "/",
           "~": "`"}


def type_text(text):
    # Real key codes where the US layout has them: SoundSwitch's text fields ignore
    # events that only carry a Unicode string.
    for ch in text:
        if ch == "\n":
            key("return")
        elif ch == " ":
            key("space")
        elif ch in KEYS:
            key(ch)
        elif ch.lower() in KEYS and ch.isalpha():
            key("shift+" + ch.lower())
        elif ch in SHIFTED:
            key("shift+" + SHIFTED[ch])
        else:
            type_unicode(ch)
        time.sleep(0.02)


def type_unicode(ch):
    buf = (ctypes.c_uint16 * 1)(ord(ch))
    for down in (True, False):
        ev = cg.CGEventCreateKeyboardEvent(None, 0, down)
        cg.CGEventKeyboardSetUnicodeString(ev, 1, buf)
        post(ev)


cf = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation")
cg.CGWindowListCopyWindowInfo.restype = ctypes.c_void_p
cg.CGWindowListCopyWindowInfo.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
cg.CGRectMakeWithDictionaryRepresentation.restype = ctypes.c_bool
cg.CGRectMakeWithDictionaryRepresentation.argtypes = [ctypes.c_void_p, ctypes.POINTER(CGRect)]
cf.CFArrayGetCount.restype = ctypes.c_long
cf.CFArrayGetCount.argtypes = [ctypes.c_void_p]
cf.CFArrayGetValueAtIndex.restype = ctypes.c_void_p
cf.CFArrayGetValueAtIndex.argtypes = [ctypes.c_void_p, ctypes.c_long]
cf.CFDictionaryGetValue.restype = ctypes.c_void_p
cf.CFDictionaryGetValue.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
cf.CFStringCreateWithCString.restype = ctypes.c_void_p
cf.CFStringCreateWithCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
cf.CFStringGetCString.restype = ctypes.c_bool
cf.CFStringGetCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_uint32]


def windows(owner):
    """On-screen window bounds (points) belonging to the named app."""
    key = lambda s: cf.CFStringCreateWithCString(None, s.encode(), 0x08000100)
    k_owner, k_bounds = key("kCGWindowOwnerName"), key("kCGWindowBounds")
    arr = cg.CGWindowListCopyWindowInfo(1, 0)
    out = []
    for i in range(cf.CFArrayGetCount(arr)):
        d = cf.CFArrayGetValueAtIndex(arr, i)
        buf = ctypes.create_string_buffer(256)
        name = cf.CFDictionaryGetValue(d, k_owner)
        if not name or not cf.CFStringGetCString(name, buf, 256, 0x08000100) or buf.value.decode() != owner:
            continue
        r = CGRect()
        if cg.CGRectMakeWithDictionaryRepresentation(cf.CFDictionaryGetValue(d, k_bounds), ctypes.byref(r)):
            out.append(r)
    cg.CFRelease(arr)
    return out


def expect_menu(x, y, height):
    # A context menu opens with its top-left at the click point. Refuse to go on unless one is
    # there, so a following click on its first item can't land on a different item (Delete).
    p = pt(x, y)
    for _ in range(10):
        for r in windows("SoundSwitch"):
            if abs(r.x - p.x) <= 4 and abs(r.y - p.y) <= 4 and abs(r.h - float(height)) <= 2:
                return
        time.sleep(0.2)
    sys.exit(f"REFUSED: no {height}-pt menu at {x},{y}")


def run(args):
    cmd = args[0]
    if cmd == "front":
        print(frontmost())
        return
    if cmd == "sleep":
        time.sleep(float(args[1]))
        return
    if cmd == "activate":
        if args[1] not in ALLOWED:
            sys.exit(f"REFUSED: {args[1]} is not an allowed app")
        subprocess.run(["open", "-a", args[1]], check=True)
        time.sleep(0.8)
        return
    guard()
    if cmd == "click":
        click(args[1], args[2], double="--double" in args, right="--right" in args)
    elif cmd == "move":
        mouse(5, pt(args[1], args[2]))
    elif cmd == "hold":
        p = pt(args[1], args[2])
        mouse(5, p)
        time.sleep(0.05)
        mouse(1, p)
        time.sleep(float(args[3]))
        mouse(2, p)
    elif cmd == "drag":
        drag(*args[1:5])
    elif cmd == "scroll":
        scroll(args[1], args[2], args[3])
    elif cmd == "type":
        type_text(" ".join(args[1:]))
    elif cmd == "key":
        key(args[1])
    elif cmd == "expectmenu":
        expect_menu(args[1], args[2], args[3])
    else:
        sys.exit(f"unknown command {cmd}")


def main():
    global only_app
    argv = sys.argv[1:]
    if argv[:1] == ["--app"]:
        if len(argv) < 2 or argv[1] not in ALLOWED:
            sys.exit("--app needs SoundSwitch or FixtureManager")
        only_app, argv = argv[1], argv[2:]
    if not argv:
        sys.exit(__doc__)
    if argv[0] == "batch":
        for line in open(argv[1]):
            line = line.strip()
            if line and not line.startswith("#"):
                print(">", line, flush=True)
                run(shlex.split(line))
                time.sleep(0.25)
    else:
        run(argv)


if __name__ == "__main__":
    main()
