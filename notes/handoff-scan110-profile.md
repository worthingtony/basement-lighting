# Handoff: custom Scan 110 profile (for Claude Code on the MacBook)

Written 2026-10-20 from a Claude chat session that had no access to the Mac's files. Read `CLAUDE.md` first for the working rules. **Ask Tony before Options > Update Fixtures.** He hasn't approved it for this job yet.

## Goal
Build one custom profile, **"Intimidator Scan 110 Claude"** (11ch), for the six I-beam scanners, and do it **in code where possible**: a script in this repo that writes or patches the profile file, so the change is repeatable and version-controlled. Fall back to clicking through Fixture Manager only if the file format turns out to be impractical. The profile has two jobs:

1. **Make them go fully dark.** They glow white at idle, and Black / zero intensity doesn't reliably kill them.
2. **Map the gobos to colors.** The Scan 110 is white only (one cool-white LED, no color wheel). Define its gobo channel as a color wheel, with a color on each gobo slot, so the Autoloop color picks the gobo.

## The fixtures

| Name in SoundSwitch | DMX | Group |
|---|---|---|
| L1 Scan 149 | 149-159 | Mover Secondary G1 |
| R1 Scan 182 | 182-192 | Mover Secondary G1 |
| L2 Scan 160 | 160-170 | Mover Secondary G2 |
| R2 Scan 193 | 193-203 | Mover Secondary G2 |
| L3 Scan 171 | 171-181 | Mover Secondary G3 |
| R3 Scan 204 | 204-214 | Mover Secondary G3 (fixture is broken but stays in programming) |

All are Intimidator Scan 110 in 11ch mode. Full patch: `notes/rig.md`.

## DMX chart, 11ch mode (from the Chauvet QRG)

| Ch | Function | Values |
|---|---|---|
| 1 | Pan | 0-255 = 0-540° |
| 2 | Pan fine | |
| 3 | Tilt | 0-255 = 0-270° |
| 4 | Tilt fine | |
| 5 | Pan/tilt speed | fast to slow |
| 6 | Gobo wheel | 0-28 open, 29-56 gobo 1, 57-85 gobo 2, 86-113 gobo 3, 114-142 gobo 4, 143-170 gobo 5, 171-199 gobo 6, 200-227 gobo 7, 228-255 gobo 8 |
| 7 | Strobe | 0-15 on, 16-131 strobe slow to fast, 132-139 on, **140-181 ramp 0-100% (slow to fast)**, 182-189 on, **190-231 ramp 100-0% (slow to fast)**, 232-239 on, 240-247 random strobe, 248-255 on |
| 8 | Dimmer | 0-255 = 0-100% |
| 9 | Function | 70-89 blackout on pan/tilt move on, 90-109 off, **110-129 blackout on gobo wheel move on**, 130-149 off, 200-209 reset all, 250-255 sound active |
| 10 | Movement macro | 16-255 = macros 1-12 |
| 11 | Macro speed | fast to slow |

There is **no shutter-closed value anywhere**: every non-strobe value on ch7 is "on". The only way to make the light dark is ch8 Dimmer = 0.

Sources: [QRG](https://www.chauvetdj.com/wp-content/uploads/2018/07/Intimidator_Scan_110_QRG_Rev2_ML6.pdf), [User Manual Rev 2](https://www.chauvetdj.com/wp-content/uploads/2018/08/Intimidator_Scan_110_UM_Rev_2.pdf).

## Job 1: going dark
Background: Tony found a Facebook thread about the sister Intimidator Spot 110 on a Wolfmix controller. Same family, same issue: the fixture has no open/closed shutter, so a controller that blacks out by "closing the shutter" leaves it on. The fix there was to give the **dimmer channel** a shutter function. The SoundSwitch equivalent:
- ch8 must be the **Dimmer / intensity** attribute, so Main Track intensity, intensity overrides and Black all drive it to 0.
- If the current profile maps ch7 as a **Shutter** with an "open/closed" range, that "closed" range is actually "on" on this light. Fix or remove it. If SoundSwitch needs a shutter attribute, see whether Fixture Manager can put Shutter on ch8 (closed = 0, open = 1-255), mirroring the Wolfmix fix.
- Existing note: `notes/fixes-and-issues.md` says the 110 profile "is fully mapped" yet they still glow. So check what the current profile actually maps before assuming.
- **Test:** CAL Test static look (Bank 4, slot 1) with only the 110s, intensity 0, then Black on the Control One. If one still glows with ch8 at 0, it's the hardware; a DMX tester is the next step.

## Job 2: gobos as colors
- In the custom profile, set ch6's attribute to **Color Wheel** instead of Gobo. Give each of the 9 ranges (open + 8 gobos) a hex color. SoundSwitch picks the wheel slot whose color is nearest the requested RGB. (It already does this for the Spots and Scan 360s; see the Scan 360 recolor in `notes/fixes-and-issues.md`.)
- **Trade-offs to tell Tony:** the beam stays white. The Gobo Change attribute cues will no longer drive the 110s. Gobos will change whenever the loop's color changes, which is fine with the slow round 2 palettes.
- **Option:** set ch9 to 110-129 (blackout while the gobo wheel moves) so changes snap cleanly. It needs a fixed value on ch9, so check whether a Fixture Manager profile can hold a default or fixed value. The earlier note says profiles have no default values, so this may need an attribute cue instead.
- Proposed mapping (by hue, chosen so the round 2 palettes land on different gobos). **Tony hasn't confirmed it, and the gobo shapes are unknown:** the manuals don't picture them. Ask Tony to film a gobo sweep, as he did for Spot 1, and reassign shapes to colors once seen.

| Color the loop asks for | Hex | 110 shows (ch6 range) |
|---|---|---|
| White | FFFFFF | Open (0-28) |
| Red | FF0000 | Gobo 1 (29-56) |
| Amber / orange | FF6E00 | Gobo 2 (57-85) |
| Yellow / warm white | FFC850 | Gobo 3 (86-113) |
| Green | 00FF00 | Gobo 4 (114-142) |
| Cyan / ice blue | 00C8FF | Gobo 5 (143-170) |
| Blue | 0028FF | Gobo 6 (171-199) |
| Violet | 6400FF | Gobo 7 (200-227) |
| Magenta / pink | FF00AA | Gobo 8 (228-255) |

- Round 2 palette colors to sanity-check against this table (from `notes/stacks.md`): 0/40/255, 40/0/255, 255/170/80, 0/160/255, 0/230/255, 255/0/0, 255/0/25, 255/110/0, 255/70/0, 255/190/120, 255/0/170, 50/0/255, 255/90/220, 0/20/255, 170/200/255, 0/0/200, 20/0/160. The nearest-color metric SoundSwitch uses is unknown, so check the result on the lights or the Ring camera.

## Strobe ramps (side note)
ch7 140-181 and 190-231 are built-in fade up / fade down effects. If the profile exposes ch7 ranges, these could give the 110s a pulse. Tony asked about a "DMX trait" for pulsing the 841 logo; Spot 1 doesn't have one, but the 110s do.

## Doing it in code
1. **Find the files.** Nothing about the on-disk format has been verified. Likely places: `~/Music/SoundSwitch` (exists, contents unseen), `~/Library/Application Support/...`, and the project itself (`/Users/tonyw/Dropbox/SoundSwitch/Claude-2100.ssproj`, the newest). Look for the Fixture Manager workspace and the existing custom profiles ("Intimidator Scan 360 Claude", "Intimidator Scan 360 Rev 2 tony") to learn the format.
2. **Back up first** into this repo. That's also item 8 in `CLAUDE.md` "Next up": back up the .ssproj and the custom profiles.
3. **Write a script** in this repo (for example `tools/scan110_profile.py`) that builds the custom profile from the stock Scan 110 profile plus the two changes, with the mapping table above as data. Never edit the stock library profile in place.
4. **Load it.** Open Fixture Manager to confirm it reads the profile cleanly, then File > Save Workspace.
5. **With Tony's OK:** in SoundSwitch, File > Save Project (as a new dated copy, for example Claude-<date>.ssproj, so Claude-2100 stays intact), then Options > Update Fixtures. Update Fixtures can crash SoundSwitch to its home screen, and it **resets the names and groups** of the updated fixtures. Restore them from the table above in the DMX patch, then save.
6. Test Job 1 and Job 2 as above. Update `notes/fixes-and-issues.md`, `notes/rig.md` (profile name), `notes/session-log.md` and `CLAUDE.md`, then commit.

## Fixture Manager facts learned so far (from `soundswitch-guide.md` and the session)
- A library profile must be renamed and saved to the workspace before it can be edited.
- Wheel slot ranges can't be reordered in the GUI, but slot colors can be changed by typing a hex code.
- Profiles hold attribute, channel and ranges; no default values.
- Name custom profiles with "Claude" so they're easy to find (Tony's request).

## Repo conventions
- Commit author: `tonyinwi <29930502+tonyinwi@users.noreply.github.com>` (the repo is public; never use Tony's personal email).
- Regular hyphens, never em dashes, in anything written for Tony.
