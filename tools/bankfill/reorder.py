# reorder.py BANK STATEFILE: drag the bank's Autoloops into flow.py's order, one insertion per slot.
# STATEFILE holds the bank's current order (original slot numbers, space-separated) and is updated after each drag.
import sys, time, importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from flow import order
spec = importlib.util.spec_from_file_location("ui", os.path.join(here, "..", "ui.py"))
ui = importlib.util.module_from_spec(spec); bank, state = int(sys.argv[1]), sys.argv[2]
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 99; sys.argv = ["ui.py"]
try: spec.loader.exec_module(ui)
except SystemExit: pass
ui.only_app = "SoundSwitch"
S = 1.31195
MX, MY = 0, 126
BANK_X = {1: 407, 2: 680, 3: 945}
X16 = [386, 522, 658, 794, 929, 1064, 1199, 1333]   # the bar-count label of each column (drag handle)
ROWS = [744, 772, 799, 827]
def M(fx, fy): return ((MX + fx * 1591 / 1421) / S, (MY + fy * 941 / 840) / S)
def slot(n): return M(X16[(n - 1) // 4], ROWS[(n - 1) % 4])

def slowdrag(a, b, hold=0.5, steps=50):
    p0, p1 = ui.pt(*a), ui.pt(*b)
    ui.guard()
    ui.mouse(5, p0); time.sleep(0.15)
    ui.mouse(1, p0); time.sleep(hold)
    for i in range(1, 6):
        ui.mouse(6, ui.CGPoint(p0.x - i * 2, p0.y)); time.sleep(0.03)
    for i in range(1, steps + 1):
        ui.mouse(6, ui.CGPoint(p0.x + (p1.x - p0.x) * i / steps, p0.y + (p1.y - p0.y) * i / steps)); time.sleep(0.03)
    time.sleep(0.6)
    ui.mouse(2, p1); time.sleep(1.2)

ui.expect_window(0, 126, 1591, 941)
if len(ui.windows("SoundSwitch")) != 1:
    sys.exit("REFUSED: another SoundSwitch window is open")
ui.guard(); ui.click(*M(BANK_X[bank], 720)); time.sleep(1.2)
# Drags only register once the slot panel has had focus (lost after a save): right-click a slot, then Escape.
r = M(313, 744)
ui.guard(); ui.click(*r, right=True)
ui.expect_menu(*r, 74)
ui.key("escape"); time.sleep(0.6)
if len(ui.windows("SoundSwitch")) != 1:
    sys.exit("REFUSED: the slot menu didn't close")
cur = [int(x) for x in open(state).read().split()]
target = order(bank)
moves = 0
for p in range(32):
    q = cur.index(target[p])
    if q == p:
        continue
    if moves >= limit:
        break
    slowdrag(slot(q + 1), slot(p + 1))
    cur.insert(p, cur.pop(q))
    open(state, "w").write(" ".join(map(str, cur)))
    moves += 1
    print(f"slot {p + 1:2d} <- was slot {q + 1:2d} (#{target[p]})", flush=True)
print("moves", moves, "final", cur == target)
