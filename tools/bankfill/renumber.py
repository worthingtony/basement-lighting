# renumber.py BANK: print a ui.py batch that renames every slot to "<prefix> <slot> <palette>" after a reorder.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import PALETTES, PREFIX, BANK_X, slot_xy, M, Mpts, S
from flow import order
bank = int(sys.argv[1])
out = ["activate SoundSwitch", "sleep 0.5", f"click {M(BANK_X[bank], 720)}", "sleep 1.2"]
for n, src in enumerate(order(bank), 1):
    if (bank, src) == (1, 17):
        continue
    name = f"{PREFIX[bank]} {n:02d} {PALETTES[bank][(src - 1) % 8][0]}"
    sx, sy = slot_xy(n)
    px, py = Mpts(sx, sy)
    out += [f"click {M(sx, sy)} --right", "sleep 0.8", f"expectmenu {px / S:.2f} {py / S:.2f} 74",
            f"click {(px + 89) / S:.1f} {(py + 12) / S:.1f}", "sleep 0.6", "key cmd+a", f"type {name}", "key return", "sleep 0.6"]
out += ["key cmd+s", "sleep 3.0"]
print("\n".join(out))
