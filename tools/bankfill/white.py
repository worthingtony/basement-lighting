# white.py PX PY: batch lines that set the open colour picker (top-left PX,PY pts) to 255,255,255 and Apply.
import sys
S = 1.31195
px, py = float(sys.argv[1]), float(sys.argv[2])
q = lambda x, y: f"{(px + x) / S:.1f} {(py + y) / S:.1f}"
out = ["activate SoundSwitch", "sleep 0.3", f"expectwin {px:g} {py:g} 580 358"]
for y in (282, 301, 320):
    out += [f"click {q(555, y)} --double", "sleep 0.25", "key cmd+a", "type 255", "key tab", "sleep 0.25"]
out += ["sleep 0.3", f"click {q(540, 345)}", "sleep 0.8"]
print("\n".join(out))
