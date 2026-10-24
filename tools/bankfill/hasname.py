# hasname.py NAME: exit 0 if the saved project's Autoloop index contains NAME.
import re, sys
d = "/Users/tonyw/Dropbox/SoundSwitch/Claude-1021.ssproj/"
names = set()
for fn in ("SoundSwitchAutoLoops.bin", "SoundSwitchAutoLoopsEx.bin"):
    b = open(d + fn, "rb").read()
    names |= {m.decode("utf-16-le") for m in re.findall(rb"(?:[\x20-\x7e]\x00){3,}", b)}
sys.exit(0 if sys.argv[1] in names else 1)
