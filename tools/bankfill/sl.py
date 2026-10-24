# sl.py ACTION ROW_Y [ARG]: drive one row of the Static Look editor (dialog at 309,610 pts, 1162x544).
# Coordinates are dialog-relative points for the layout where some row's movement settings are expanded:
# include 189, colour 222, intensity 256->370, position 420, movement-settings dots 481, movement 555.
import sys, time, importlib.util
spec = importlib.util.spec_from_file_location("ui", __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "ui.py"))
ui = importlib.util.module_from_spec(spec); sys.argv, argv = ["ui.py"], sys.argv
try: spec.loader.exec_module(ui)
except SystemExit: pass
ui.only_app = "SoundSwitch"
S = ui.SCALE if hasattr(ui, "SCALE") else 1.31195
X, Y = 309, 610
PROMPT = (760, 1040, 230, 598)

def wins():
    return [(r.x, r.y, r.w, r.h) for r in ui.windows("SoundSwitch")]

def need(bounds):
    for _ in range(15):
        if any(all(abs(a - b) <= 2 for a, b in zip(w, bounds)) for w in wins()):
            return
        time.sleep(0.2)
    sys.exit(f"REFUSED: no window {bounds}; have {wins()}")

def at(x, y):  # absolute points -> ui coords, refusing the permission prompt
    if PROMPT[0] <= x <= PROMPT[1] and PROMPT[2] <= y <= PROMPT[3]:
        sys.exit(f"REFUSED: {x},{y} is on the permission prompt")
    return x / S, y / S

def click(x, y, **kw):
    ui.guard(); ui.click(*at(x, y), **kw); time.sleep(0.6)

def drag(x1, y1, x2, y2):
    ui.guard(); ui.drag(*at(x1, y1), *at(x2, y2)); time.sleep(0.5)

def popup(w, h):  # any open dropdown list: 220 tall, narrower than the dialog
    for _ in range(15):
        for b in wins():
            if abs(b[3] - h) <= 2 and b[2] < 400:
                return b
        time.sleep(0.2)
    sys.exit(f"REFUSED: no {w}x{h} popup; have {wins()}")

POS = ["THRU", "Floor Center", "Front of Floor", "Tiny Ball", "Back of Floor", "Cross", "Lanes", "Ball", "841 Logo", "DJ Booth"]
MOV = ["No Movement", "Circle", "Scan Horizontal", "Scan Vertical", "Oval Horizontal", "Oval Vertical", "Figure 8 Horizontal",
       "Figure 8 Vertical", "Square", "Triple 8 Horizontal"]

import os
# Column x per layout: "narrow" while an expanded row (Size/Speed) is in view, "wide" otherwise.
C = {"narrow": dict(inc=189, col=222, i0=256, i1=375, pos=420, dots=481, mov=555),
     "medium": dict(inc=219, col=251, i0=286, i1=398, pos=450, dots=511, mov=575),
     "wide2": dict(inc=259, col=292, i0=326, i1=442, pos=490, dots=551, mov=595),
     "vwide": dict(inc=352, col=385, i0=420, i1=535, pos=0, dots=0, mov=0),
     "wide": dict(inc=244, col=277, i0=311, i1=430, pos=475, dots=536, mov=580)}[os.environ.get("L", "narrow")]
act, ry = argv[1], float(argv[2])
arg = " ".join(argv[3:]) or None
subprocess = ui.subprocess
subprocess.run(["open", "-a", "SoundSwitch"]); time.sleep(0.5)
need((X, Y, 1162, 544))
if act == "include":
    click(X + C['inc'], Y + ry)
elif act == "full":
    drag(X + C['i0'], Y + ry, X + C['i1'], Y + ry)
elif act == "pos":
    click(X + C['pos'], Y + ry)
    b = popup(101, 220)
    click(b[0] + 50, b[1] + 11 + 22 * POS.index(arg))
elif act == "mov":
    click(X + C['mov'], Y + ry)
    b = popup(115, 220)
    click(b[0] + 50, b[1] + 11 + 22 * MOV.index(arg))
elif act == "dots":
    click(X + C['dots'], Y + ry)
elif act == "size":  # ARG = dialog-relative x for the Size handle, on the Size line at ROW_Y
    drag(X + 578, Y + ry, X + float(arg), Y + ry)
elif act == "speed":
    drag(X + 578, Y + ry, X + float(arg), Y + ry)
elif act == "white":
    click(X + C['col'], Y + ry, double=True)
    time.sleep(0.6)
    need((889, 710, 580, 358))
    for fy in (282, 301, 320):
        click(889 + 555, 710 + fy, double=True); ui.key("cmd+a"); ui.type_text("255"); ui.key("tab"); time.sleep(0.25)
    click(889 + 540, 710 + 345)
else:
    sys.exit("unknown action")
print("ok", act, ry, arg or "")
