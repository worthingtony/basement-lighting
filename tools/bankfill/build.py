# Generate tools/ui.py batches that build one Autoloop with the approved recipe.
# Usage: build.py PHASE BANK SLOT   (PHASE = A: open + fill the Autoscript dialog; B: apply, cues, rename, save)
# Geometry: SoundSwitch main window at (99,143) pts, 1591x941, screenshot frame 1421x840.
# Autoscript dialog at (445,39) pts, colour picker at (794,267), preset list at (454,89).
import sys

import os
S = 1.31195
MX, MY = float(os.environ.get("MX", 99)), float(os.environ.get("MY", 143))
DX, DY = float(os.environ.get("DX", 445)), float(os.environ.get("DY", 39))
def M(fx, fy):  # main-window frame -> ui.py coords
    return f"{(MX + fx * 1591 / 1421) / S:.1f} {(MY + fy * 941 / 840) / S:.1f}"
def Mpts(fx, fy):
    return MX + fx * 1591 / 1421, MY + fy * 941 / 840
def D(x, y):
    return f"{(DX + x) / S:.1f} {(DY + y) / S:.1f}"
def P(x, y):  # colour picker opens 349,228 pts from the dialog
    return f"{(DX + 349 + x) / S:.1f} {(DY + 228 + y) / S:.1f}"
def L(x, y):  # preset list opens 9,50 pts from the dialog
    return f"{(DX + 9 + x) / S:.1f} {(DY + 50 + y) / S:.1f}"

BANK_X = {1: 407, 2: 680, 3: 945}
COLS = [313, 450, 595, 735, 870, 1005, 1140, 1278]
ROWS = [744, 772, 799, 827]
def slot_xy(n):
    return COLS[(n - 1) // 4], ROWS[(n - 1) % 4]

PRESET_Y = {"Dyn1": 54, "Dyn2": 76, "Dyn3": 99, "Dyn4": 121, "Dyn5": 143, "Dyn6": 165, "Dance1": 187}
ROW = {"FC": 373, "Front": 395, "Back": 439, "Cross": 461, "Lanes": 483}
VARIANTS = [
    (["FC", "Cross", "Lanes", "Back"], ["Front", "Cross", "FC", "Lanes"]),
    (["Front", "Lanes", "Back", "Cross"], ["FC", "Back", "Cross", "Front"]),
    (["Cross", "FC", "Lanes"], ["Lanes", "Front", "Back"]),
    (["Back", "Front", "FC", "Lanes"], ["Cross", "Lanes", "FC"]),
]
W = (255, 255, 255)
PALETTES = {
    1: [  # tech house groove
        ("Blue Magenta", [(0, 40, 255), (255, 0, 160), (120, 0, 255), W]),
        ("Amber Blue", [(255, 110, 0), (0, 60, 255), (255, 170, 80), (200, 220, 255)]),
        ("Teal Magenta", [(0, 200, 170), (255, 0, 150), (0, 120, 255), W]),
        ("Blue Warm", [(0, 30, 255), (255, 170, 80), (0, 100, 255), (255, 220, 180)]),
        ("Violet Pink", [(120, 0, 255), (255, 60, 180), (60, 0, 200), (255, 200, 240)]),
        ("Amber Magenta", [(255, 120, 0), (255, 0, 140), (255, 60, 0), (255, 180, 100)]),
        ("Cyan Blue", [(0, 180, 255), (0, 40, 255), (0, 255, 220), W]),
        ("Red White", [(255, 0, 0), W, (180, 0, 30), (255, 200, 200)]),
    ],
    2: [  # 80s / 90s
        ("Neon Pink Cyan", [(255, 0, 170), (0, 230, 255), (170, 0, 255), W]),
        ("Miami", [(0, 220, 200), (255, 80, 180), (255, 150, 200), W]),
        ("Sunset", [(255, 80, 0), (255, 0, 120), (160, 0, 255), (255, 200, 100)]),
        ("Purple Gold", [(140, 0, 255), (255, 180, 0), (90, 0, 200), (255, 230, 150)]),
        ("Pink Yellow", [(255, 0, 130), (255, 220, 0), (255, 100, 0), W]),
        ("Electric Blue", [(0, 80, 255), (255, 0, 200), (0, 200, 255), W]),
        ("Red Blue", [(255, 0, 40), (0, 60, 255), (180, 0, 255), W]),
        ("Lavender Teal", [(180, 120, 255), (0, 210, 190), (255, 120, 220), W]),
    ],
    3: [  # tech house peak
        ("Red White", [(255, 0, 0), W, (200, 0, 40), (255, 220, 220)]),
        ("Ice Blue", [(200, 220, 255), (0, 60, 255), W, (120, 160, 255)]),
        ("Magenta Red", [(255, 0, 120), (255, 0, 0), (255, 0, 200), W]),
        ("Gold White", [(255, 160, 0), W, (255, 100, 0), (255, 230, 180)]),
        ("UV Purple", [(90, 0, 255), (180, 0, 255), (40, 0, 160), W]),
        ("Blue Red", [(0, 40, 255), (255, 0, 0), (0, 0, 180), W]),
        ("Pink Cyan", [(255, 0, 160), (0, 200, 255), (200, 0, 255), W]),
        ("Orange Teal", [(255, 90, 0), (0, 190, 170), (255, 150, 0), W]),
    ],
}
PRESETS = {1: ["Dance1", "Dyn1", "Dance2", "Dyn2", "Dyn3"], 2: ["Dyn1", "Dyn2", "Dance2", "Dyn5", "Dyn6", "RC1"],
           3: ["Dyn4", "Dyn5", "Dance2", "Dyn6", "Dance1", "RC2"]}
INDEX = {"Dyn1": 1, "Dyn2": 2, "Dyn3": 3, "Dyn4": 4, "Dyn5": 5, "Dyn6": 6, "Dance1": 7, "Dance2": 8, "RC1": 9, "RC2": 10}  # rows below Base Styles
PREFIX = {1: "TH", 2: "80s", 3: "PK"}
BAR = lambda n: 283 + (n - 1) * 66.85
# Shocker cues per bank: (cue, bar). "P" = this loop's program.
CUES = {
    1: [("Off", 1), ("P", 9), ("Prism", 10), ("Off", 11), ("P", 13), ("Off", 15)],
    2: [("Off", 1), ("Prism", 10), ("P", 13), ("Off", 15)],
    3: [("Off", 1), ("P", 5), ("Off", 7), ("P", 9), ("Prism", 10), ("Off", 11), ("P", 13), ("Off", 15)],
}
# Cue list rows: list scrolled to the bottom / to the top.
BOTTOM = {"P4": 692, "P5": 712, "P6": 731, "P7": 751, "P8": 770, "Off": 829}
TOP = {"Prism": 691, "P1": 730, "P2": 750, "P3": 770}


def spec(bank, slot):
    i = slot - 1
    pal_name, pal = PALETTES[bank][i % 8]
    variant = VARIANTS[(i // 8) % 4]
    preset = PRESETS[bank][(i // 8 + i) % len(PRESETS[bank])]
    program = f"P{(i * 3) % 8 + 1}"
    name = f"{PREFIX[bank]} {slot:02d} {pal_name}"
    return dict(pal=pal, variant=variant, preset=preset, program=program, name=name)


def phase_a(bank, slot):
    s = spec(bank, slot)
    sx, sy = slot_xy(slot)
    out = ["activate SoundSwitch", "sleep 0.6",
           f"click {M(BANK_X[bank], 720)}", "sleep 1.2",
           f"click {M(sx, sy)} --double", "sleep 2.0",
           f"click {M(901, 90)}", "sleep 2.0"]
    # The dialog opens at (445,39); a macOS prompt sits over its middle, so drag it to (DX,DY).
    out += ["expectwin 445 39 700 800", f"drag {600 / S:.1f} {51 / S:.1f} {(600 + DX - 445) / S:.1f} {(51 + DY - 39) / S:.1f}",
            "sleep 1.0", f"expectwin {DX:g} {DY:g} 700 800"]
    return out


def phase_a2(bank, slot):
    s = spec(bank, slot)
    out = ["activate SoundSwitch", "sleep 0.5", f"expectwin {DX:g} {DY:g} 700 800"]
    # Keyboard only: the list scrolls to the current preset, so clicking rows by position is unreliable.
    # Two passes: Up x12 + Return lands on Base Styles; a fresh open then counts down from there.
    out += [f"click {D(247, 42)}", "sleep 1.0"] + ["key up", "sleep 0.15"] * 12 + ["key return", "sleep 1.5"]
    out += [f"click {D(247, 42)}", "sleep 1.0"] + ["key down", "sleep 0.3"] * INDEX[s["preset"]] + ["key return", "sleep 1.5"]
    out += [
           f"drag {D(77, 110)} {D(110, 160)}", "sleep 0.5",
           f"drag {D(495, 110)} {D(455, 104)}", "sleep 0.5"]
    for col_x, rows in ((476, s["variant"][0]), (522, s["variant"][1])):
        for r in rows:
            out += [f"click {D(col_x, ROW[r])}", "sleep 0.35"]
    out += [f"click {D(512, 206)}", "sleep 0.6"]
    for sw_x, (r, g, b) in zip((99, 266, 433, 600), s["pal"]):
        out += [f"click {D(sw_x, 262)}", "sleep 1.4"]
        for (fx, fy), v in (((555, 282), r), ((555, 301), g), ((555, 320), b)):
            out += [f"click {P(fx, fy)} --double", "sleep 0.25", "key cmd+a", f"type {v}", "key tab", "sleep 0.25"]
        out += ["sleep 0.3", f"click {P(540, 345)}", "sleep 1.0"]
    return out


def phase_b(bank, slot):
    s = spec(bank, slot)
    prog = s["program"]
    out = ["activate SoundSwitch", "sleep 0.5", f"expectwin {DX:g} {DY:g} 700 800",
           f"click {D(660, 787)}", "sleep 4.0",
           f"click {D(574, 787)}", "sleep 1.5"]
    plan = [(prog if c == "P" else c, bar) for c, bar in CUES[bank]]
    def drops(rows):
        o = []
        for cue, bar in plan:
            if cue in rows:
                o += [f"click {M(60, rows[cue])}", "sleep 0.4", f"drag {M(60, rows[cue])} {M(BAR(bar), 626)}", "sleep 0.8"]
        return o
    out += [f"drag {M(263, 705)} {M(263, 840)}", "sleep 1.0"] + drops(BOTTOM)
    out += [f"drag {M(263, 820)} {M(263, 640)}", "sleep 1.0"] + drops(TOP)
    # rename the slot, guarded so the click can only hit the menu's first item (Rename)
    sx, sy = slot_xy(slot)
    px, py = Mpts(sx, sy)
    out += [f"click {M(sx, sy)} --right", "sleep 1.0",
            f"expectmenu {px / S:.2f} {py / S:.2f} 74",
            f"click {(px + 89) / S:.1f} {(py + 12) / S:.1f}", "sleep 0.8",
            "key cmd+a", f"type {s['name']}", "key return", "sleep 0.8",
            "key cmd+s", "sleep 3.0"]
    return out


if __name__ == "__main__":
    phase, bank, slot = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if phase == "spec":
        print(spec(bank, slot))
    else:
        lines = {"A": phase_a, "A2": phase_a2, "B": phase_b}[phase](bank, slot)
        # Never click or drag inside the macOS permission prompt (UserNotificationCenter, 770,240 260x348 pts).
        for ln in lines:
            p = ln.split()
            if p and p[0] in ("click", "drag"):
                v = [float(t) * S for t in p[1:5] if t[0].isdigit()]
                for x, y in zip(v[0::2], v[1::2]):
                    if 760 <= x <= 1040 and 230 <= y <= 598:
                        sys.exit(f"REFUSED: {ln} lands on the permission prompt")
        print("\n".join(lines))
