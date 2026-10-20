# Handoff: custom Scan 110 and Vortex profiles (for Claude Code on the MacBook)

Written 2026-10-20 from a Claude chat session that had no access to the Mac's files; the Vortex part was added the same afternoon from a cloud session, working from the Vortex manual. Read `CLAUDE.md` first for the working rules. **Ask Tony before Options > Update Fixtures.** He hasn't approved it for this job yet.

Manuals for both fixtures are in `manuals/` (index: `manuals/README.md`).

## Goal
Build two custom profiles in one Fixture Manager session, then apply both with **one** Update Fixtures pass. Do it **in code where possible**: a script in this repo that writes or patches the profile files, so the change is repeatable and version-controlled. Fall back to clicking through Fixture Manager only if the file format turns out to be impractical.

1. **"Intimidator Scan 110 Claude"** (11ch), for the six I-beam scanners:
   - **Make them go fully dark.** They glow white at idle, and Black / zero intensity doesn't reliably kill them.
   - **Map the gobos to colors.** The Scan 110 is white only (one cool-white LED, no color wheel). Define its gobo channel as a color wheel, with a color on each gobo slot, so the Autoloop color picks the gobo.
2. **"Eliminator Vortex Claude"** (12ch), for F Vortex 405:
   - **Make Black stop it**, and find its idle glow. Test first (below); the fix depends on the result.
   - **Give it color.** Its gobo wheel *is* its color wheel (colored gobos), so map that channel as a color wheel and the Autoloops can color it.

---

# Scan 110

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

Sources: `manuals/chauvet-intimidator-scan-110-qrg-rev2.pdf` and `manuals/chauvet-intimidator-scan-110-user-manual-rev2.pdf` (originals: [QRG](https://www.chauvetdj.com/wp-content/uploads/2018/07/Intimidator_Scan_110_QRG_Rev2_ML6.pdf), [User Manual Rev 2](https://www.chauvetdj.com/wp-content/uploads/2018/08/Intimidator_Scan_110_UM_Rev_2.pdf)). Chart re-checked against the QRG on 2026-10-20.

## Job 1: going dark
Background: Tony found a Facebook thread about the sister Intimidator Spot 110 on a Wolfmix controller. Same family, same issue: the fixture has no open/closed shutter, so a controller that blacks out by "closing the shutter" leaves it on. The fix there was to give the **dimmer channel** a shutter function. The SoundSwitch equivalent:
- ch8 must be the **Dimmer / intensity** attribute, so Main Track intensity, intensity overrides and Black all drive it to 0.
- If the current profile maps ch7 as a **Shutter** with an "open/closed" range, that "closed" range is actually "on" on this light. Fix or remove it. If SoundSwitch needs a shutter attribute, see whether Fixture Manager can put Shutter on ch8 (closed = 0, open = 1-255), mirroring the Wolfmix fix.
- Existing note: `notes/fixes-and-issues.md` says the 110 profile "is fully mapped" yet they still glow. So check what the current profile actually maps before assuming.
- **Test:** CAL Test static look (Bank 4, slot 1) with only the 110s, intensity 0, then Black on the Control One. If one still glows with ch8 at 0, it's the hardware; a DMX tester is the next step.

## Job 2: gobos as colors
- In the custom profile, set ch6's attribute to **Color Wheel** instead of Gobo. Give each of the 9 ranges (open + 8 gobos) a hex color. SoundSwitch picks the wheel slot whose color is nearest the requested RGB. (It already does this for the Spots and Scan 360s; see the "Intimidator Scan 360 Claude" recolor on 2026-10-06 22:10 in `notes/session-log.md`.)
- **Trade-offs to tell Tony:** the beam stays white. The Gobo Change attribute cues will no longer drive the 110s. Gobos will change whenever the loop's color changes, which is fine with the slow round 2 palettes.
- **Option:** set ch9 to 110-129 (blackout while the gobo wheel moves) so changes snap cleanly. It needs a fixed value on ch9, so check whether a Fixture Manager profile can hold a default or fixed value. The earlier note says profiles have no default values, so this may need an attribute cue instead.
- Proposed mapping (by hue, chosen so the round 2 palettes land on different gobos). **Tony hasn't confirmed it.** The QRG pictures the 8 gobos (page 3, PDF page 4); the shapes below are read from that picture. Tony may want to pair shapes and colors by taste, and a filmed gobo sweep (as he did for Spot 1) would confirm his units match the picture.

| Color the loop asks for | Hex | 110 shows (ch6 range) | Gobo shape (QRG picture) |
|---|---|---|---|
| White | FFFFFF | Open (0-28) | none |
| Red | FF0000 | Gobo 1 (29-56) | three curved blades |
| Amber / orange | FF6E00 | Gobo 2 (57-85) | spiral |
| Yellow / warm white | FFC850 | Gobo 3 (86-113) | slanted bars |
| Green | 00FF00 | Gobo 4 (114-142) | sunburst rays |
| Cyan / ice blue | 00C8FF | Gobo 5 (143-170) | two swirls |
| Blue | 0028FF | Gobo 6 (171-199) | dot cluster |
| Violet | 6400FF | Gobo 7 (200-227) | shattered glass |
| Magenta / pink | FF00AA | Gobo 8 (228-255) | broken ring |

- Round 2 palette colors to sanity-check against this table (from `notes/stacks.md`): 0/40/255, 40/0/255, 255/170/80, 0/160/255, 0/230/255, 255/0/0, 255/0/25, 255/110/0, 255/70/0, 255/190/120, 255/0/170, 50/0/255, 255/90/220, 0/20/255, 170/200/255, 0/0/200, 20/0/160. The nearest-color metric SoundSwitch uses is unknown, so check the result on the lights or the Ring camera.

## Strobe ramps (side note)
ch7 140-181 and 190-231 are built-in fade up / fade down effects. If the profile exposes ch7 ranges, these could give the 110s a pulse. Tony asked about a "DMX trait" for pulsing the 841 logo; Spot 1 doesn't have one, but the 110s do.

---

# Vortex

## The fixture

| Name in SoundSwitch | DMX | Group |
|---|---|---|
| F Vortex 405 | 405-416 | Mover Tertiary G1 |

Eliminator Vortex (VOR100) in 12ch mode. Confirm the fixture's own menu reads DMX Settings > DMX CH Mode = **12CH**.

## DMX chart, 12ch mode (Vortex user manual, pages 22-26)

| Ch | Function | Values |
|---|---|---|
| 1 | Pan | 0-255 |
| 2 | Tilt (barrel rotation) | 0-9 stop, 10-120 counter-clockwise fast to slow, 121-134 stop, 135-245 clockwise slow to fast, 246-255 stop |
| 3 | Gobo / color wheel | 0-7 open (white big spots), 8-13 gobo 1 red tri-bar, 14-19 gobo 2 blue hazard, 20-25 gobo 3 green triangle, 26-31 gobo 4 yellow shattered glass, 32-37 gobo 5 RGBY multicolor quad dots, 38-43 gobo 6 magenta square rays, 44-49 gobo 7 aqua four-point star, 50-55 gobo 8 lime multi dots, 56-64 gobo 9 white small dots. 65-127 = the same gobos with shake, slow to fast. 128-255 = automatic gobo change, slow to fast |
| 4 | Reflector rotation | 0-9 stop, 10-120 clockwise slow to fast, 121-134 stop, 135-245 counter-clockwise fast to slow, 246-255 stop |
| 5 | Shutter | **0-31 closed**, 32-63 open, 64-95 strobe slow to fast, 96-127 open, 128-159 pulse effect in sequences, 160-191 open, 192-223 random strobe slow to fast, 224-255 open |
| 6 | Dimmer | 0-255 = 0-100% |
| 7 | Show | 0-15 off, 16-46 Show 1, 47-77 Show 2, 78-108 Show 3, 109-139 Show 4, 140-170 Show 5, 171-201 Show 6, 202-255 Show 0 (random 1-6) |
| 8 | Show speed | slow to fast |
| 9 | Dim mode / dim speed | 0-20 unit setting; 21-140 dim modes in steps of 20 (Standard, Stage, TV, Architectural, Theatre, Stage 2); 141-160 dim speed 0.1-10 s; 161-255 unit setting |
| 10 | Dim curve | 0-20 square, 21-40 linear, 41-60 inverse square, 61-80 S curve, 81-255 no function |
| 11 | Pan speed | fast to slow |
| 12 | Special | resets, pan/tilt invert, LED refresh rate, sound on/off (each needs the value held for 1-5 s). Leave at 0 |

Unlike the Scan 110, the Vortex **does** have a closed shutter (ch5 0-31).

What it runs now (`notes/calibration.md`): "Vortex Show" = Show 134, which is **Show 4**, with Barrel Rotation 65 (ch2, medium counter-clockwise). Vortex Slow / Medium / Fast use Show Speed 10 / 120 / 230. There are only 6 built-in programs, so "try more Show values" means these: **31, 62, 93, 124, 155, 186** (Shows 1-6) and **228** (random).

## Job V1: Black and the idle glow (test before changing the profile)
Tony saw Black leave the Vortex running while Vortex Show was on. Likely cause: while ch7 runs a built-in show, the fixture runs its own program and may ignore ch5 and ch6. Test in CAL Test (Bank 4, slot 1), Vortex only, Show 124 and Barrel Rotation 65:
1. Dimmer 0. Does it go dark?
2. Dimmer full, shutter closed (ch5 below 32). Does it go dark? This is only possible if the current profile exposes ch5; check what the stock profile maps there.
3. Show 0-15 (off). Does it stop?
4. Have Tony set the Vortex's own display to **Information > DMXValue**, then press Black on the Control One. The fixture shows what it receives on each channel, so it doubles as a DMX tester. Note what Black actually sends on ch5, ch6 and ch7.

Fix, by result:
- **Dimmer 0 or shutter closed kills it during a show:** the custom profile maps ch6 as Dimmer / intensity and ch5 as Shutter (closed 0-31, open 32-63, strobe 64-95), so Black drives whichever one works.
- **Only Show off stops it:** no profile can make Black stop the built-in show. Either add a "Vortex Off" static look (Show off, dimmer 0) to press along with Black, or retire Vortex Show for Autoloop-driven Vortex looks once V2 is done (color from ch3, plus Barrel and Reflector Rotation attribute cues).

**Idle glow:** with nothing programmed in Edit mode, read Information > DMXValue during the glow. If ch5 is below 32 or ch6 is 0 and it still glows, it's the fixture. If not, SoundSwitch is sending something, so look at the profile. Separately, Tony can set DMX Settings > **No DMX Status** to **Blackout** on the fixture (options: Hold, Blackout, Show, Manual). That's the Vortex's share of cleanup item 6 in `CLAUDE.md`.

## Job V2: color from the gobo wheel
- In the custom profile, set ch3's attribute to **Color Wheel**, with 10 slots: open plus gobos 1-9, using only the 0-64 static ranges. Leave out the shake ranges (65-127) and auto change (128-255): auto change spins through the wheel, which Tony doesn't want ("respect the color wheels").
- The colors are real here (colored gobos), unlike the Scan 110. The wheel is pictured on page 27 of the manual.
- Proposed slot colors. **Tony hasn't confirmed them.** The hex is what a loop would ask for, so nearest-color lands sensibly.

| Slot | ch3 range | Gobo | Hex |
|---|---|---|---|
| Open | 0-7 | white big spots | FFFFFF |
| 1 | 8-13 | red tri-bar | FF0000 |
| 2 | 14-19 | blue hazard | 0040FF |
| 3 | 20-25 | green triangle | 00FF00 |
| 4 | 26-31 | yellow shattered glass | FFC850 |
| 5 | 32-37 | RGBY multicolor quad dots | 808000 (see below) |
| 6 | 38-43 | magenta square rays | FF00AA |
| 7 | 44-49 | aqua four-point star | 00C8FF |
| 8 | 50-55 | lime multi dots | A0FF40 |
| 9 | 56-64 | white small dots | AAC8FF (ice white) |

- **Slot 5 is multicolor**, so no single color fits. Recommendation: give it a color the palettes never ask for (olive 808000, above), so it's only reached on purpose. Alternative: orange FF6E00 (the manual's shake list calls it "orange quad dots"), but then every orange loop shows multicolor dots, which works against Tony's one-palette looks. Tony decides.
- **No orange or violet slot.** Orange loops will land on red or yellow, and violet loops on blue.
- **Ice white on slot 9** sends pure white to the big open spots and the round 2 ice color (170/200/255) to the small dots.
- Check with the same round 2 palette list as the Scan 110, on the lights or the Ring camera.

## Pulse (side note)
ch5 128-159 is a built-in "pulse effect in sequences", another candidate for the pulse Tony asked about.

---

# Doing it in code (both profiles)
1. **Find the files.** Nothing about the on-disk format has been verified. Likely places: `~/Music/SoundSwitch` (exists, contents unseen), `~/Library/Application Support/...`, and the project itself (`/Users/tonyw/Dropbox/SoundSwitch/Claude-2100.ssproj`, the newest). Look for the Fixture Manager workspace and the existing custom profiles ("Intimidator Scan 360 Claude", "Intimidator Scan 360 Rev 2 tony") to learn the format.
2. **Back up first** into this repo. That's also item 8 in `CLAUDE.md` "Next up": back up the .ssproj and the custom profiles.
3. **Write a script** in this repo (for example `tools/fixture_profiles.py`) that builds each custom profile from its stock profile plus the changes above, with the mapping tables as data. Never edit the stock library profile in place.
4. **Load them.** Open Fixture Manager to confirm it reads both profiles cleanly, then File > Save Workspace.
5. **With Tony's OK:** in SoundSwitch, File > Save Project (as a new dated copy, for example Claude-<date>.ssproj, so Claude-2100 stays intact), then Options > Update Fixtures. Update Fixtures can crash SoundSwitch to its home screen, and it **resets the names and groups** of the updated fixtures. Restore them from the two fixture tables above in the DMX patch, then save.
6. **Check the existing Vortex looks** still hold their values after the update: CAL Test, Vortex Show, Vortex Slow / Medium / Fast (Show, Show Speed, Barrel Rotation).
7. Test Jobs 1, 2, V1 and V2 as above. Update `notes/fixes-and-issues.md`, `notes/rig.md` (profile names), `notes/calibration.md`, `notes/session-log.md` and `CLAUDE.md`, then commit.

## Fixture Manager facts learned so far (from `soundswitch-guide.md` and the sessions)
- A library profile must be renamed and saved to the workspace before it can be edited.
- Wheel slot ranges can't be reordered in the GUI, but slot colors can be changed by typing a hex code.
- Profiles hold attribute, channel and ranges; no default values.
- "Intimidator Scan 360 Claude" kept **the same ID as the stock profile**, and Update Fixtures then applied it to the already-patched fixtures (2026-10-06 22:10, `notes/session-log.md`). Expect the same approach to work here.
- Name custom profiles with "Claude" so they're easy to find (Tony's request).

## Repo conventions
- Commit author: `tonyinwi <29930502+tonyinwi@users.noreply.github.com>` (the repo is public; never use Tony's personal email).
- Regular hyphens, never em dashes, in anything written for Tony.
