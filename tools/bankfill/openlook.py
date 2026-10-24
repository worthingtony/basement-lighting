# openlook.py FX FY: open the Static Look editor for the look at main-window frame (FX,FY) and move it to (309,610).
import sys, time, importlib.util
spec = importlib.util.spec_from_file_location("ui", __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "ui.py"))
ui = importlib.util.module_from_spec(spec); fx, fy = float(sys.argv[1]), float(sys.argv[2]); sys.argv = ["ui.py"]
try: spec.loader.exec_module(ui)
except SystemExit: pass
ui.only_app = "SoundSwitch"
S = 1.31195
px, py = fx * 1591 / 1421, 126 + fy * 941 / 840
ui.guard(); ui.click(px / S, py / S, right=True)
ui.expect_menu(px / S, py / S, 118)
ui.click((px + 60) / S, (py + 45) / S)  # Edit (third item)
time.sleep(2.0)
ui.expect_window(309, 292, 1162, 544)
ui.drag(600 / S, 304 / S, 600 / S, 622 / S); time.sleep(1.0)
ui.expect_window(309, 610, 1162, 544)
print("editor open at 309,610")
