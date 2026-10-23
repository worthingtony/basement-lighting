# SoundSwitch knowledge base: what matters for Studio 841

Read on 2026-10-20 from support.soundswitch.com: all 10 folders (131 articles) were listed and about 70 of the relevant ones were read. Many KB articles are only stubs for a video. "(inferred)" marks anything that isn't stated in the KB. Article links are at the bottom.

## Tempo sources: Ableton Link, BPM Detection, others
- **Link** syncs Autoloops, Static Looks and MIDI overrides to any Link app on **the same local network** (Serato, Live, Traktor, rekordbox). [link]
  - To switch it on: the Link button at the top left of Performance Mode, or **Shift + BPM TAP** on the Control One. Turning it on disconnects SoundSwitch from any DJ software. [standalone] [c1pdf]
  - The KB doesn't say what Link syncs. (inferred, from Ableton's docs: tempo, beat and phase.)
- **Source Selection** offers Ableton Link, BPM Detection, MIDI, DJ Software, and PRO DJ LINK (new in 2.11). [ui29] [pdl]
- **BPM Detection** (Preferences > Tempo Detection) is the fallback that works with any DJ. [bpm] [band] [bpmaudio]
  - Audio input: a **USB audio interface works best**. The laptop mic is the least reliable, and macOS needs microphone permission for it.
  - Keep the VU meter in the green.
  - Refresh rate: 5 s for open-format sets, 10 s for steady house.
  - Set a BPM range (for example 70-140) and an audio threshold.
  - After 3 s below the threshold it goes to Blackout or "Pause Autoloop" (your choice).
  - To change the source: disable it, change it, then re-enable.
- **Manual tempo:** BPM Tap, the BPM knob, fine steps of 0.1 and 0.5, beat and phase shift. [standalone]
- **MIDI Clock / MTC in** drives Autoloops only. [midisync]
- **PRO DJ LINK Bridge:** for CDJ-3000/2000NXS2 and similar decks, through a free AlphaTheta app. [pdl]
- **Traktor and djay:** Link or BPM Detection only (no scripted tracks). [compat]

## Control One
- **AUTO LOOP** switches the 32 pads between Autoloops and Static Looks. [c1pdf]
- **AUTOLOOP OVERRIDE** ignores scripted tracks and plays Autoloops only. [c1pdf]
- **BANK buttons** [al29]
  - Long-press = exclusive bank. It takes effect when the current loop ends, or when you trigger a loop by hand.
  - Shift + bank = Play All Banks.
  - Bank LEDs: white = selected, pulsing blue = playing, pulsing red = exclusive. The playing Autoloop's pad flashes.
- **MOVEMENT / STROBE / HUE / SMOKE** launch effects. The knobs set their "Effect Speed & Color". The KB never says what each sends. [c1pdf]
- **Color pads:**
  - Color overrides; Shift + pad = Position 1-9. The KB doesn't say how positions map. (inferred: library order; press them to check.)
  - Pad LED colors: in the MIDI screen, right-click a button > MIDI Output Color. [c1faq]
- **WHITE / BLACK / UV:** full white, blackout and UV. The guide says Shift toggles them, but on Tony's unit a plain press of BLACK is already a toggle (2026-10-20). The printed HOLD labels are presumably the Shift (momentary) versions. [c1pdf]
- **Touch strip:** Autoloop or scripted intensity, or Group 1-4 intensity. [c1pdf]
- **Two DMX universes.** Address a fixture as `2:100`, or pick the universe in the DMX chart. [univ]
- **USB 1/2 switch:** two hosts at once. It always needs a computer running SoundSwitch 2.5+. [c1faq] [omni]
- **Firmware:** latest v1.18, updated over USB port 1. [c1fw]
- **Export to Control One:** sends one venue (Autoloops, Static Looks; no scripted tracks). It is "not a backup". [c1exp]

## Autoloops
- 4 banks of 32. Lengths are 8/16/32/64/128 bars. A loop advances when it ends. (inferred: no phrase detection.) [alx] [al29]
- **Repeat** (Preferences > Performance Mode): Infinite, or Track Duration, where a new track starts a new loop. With Link there's no track information, so Infinite is the setting that applies. (inferred) [al29]
- **Autoscript** [ascript] [new28]
  - Choose a preset, then which Position and Attribute Cues to use and in what order.
  - Presets react to the fixture categories set on the DMX page.
  - Movement can be left out. Right-click a fixture to exclude it.
- **Attribute cues are global:** editing one changes every Autoloop that uses it. [attr]
- **Effects Generator, Forward Chase:** a per-fixture chase. This is the tool for stepping the Tripars down the floor. [fxgen]
- **Movement shapes:** size and speed can ramp across the selection. [shapes]
- **Track precedence:** Fixture and Group tracks override the Master Track. [ctrl]
- **Hot keys:** Shift+P position override, Shift+O override, Shift+S strobe, Shift+T color transition, keys 1-0 intensity pulses. [keys]
- **KB advice:** "Solid color loops, color transition effects, and slow intensity fades tend to work well." [alx]

## Static Looks (2.11)
- 4 renameable banks of 32. Several can be active at once. For each fixture and parameter, the most recently triggered look wins. [sl211]
- **Thru per parameter** (Color, Intensity, Position, Movement, Strobe, Attributes) lets the Autoloop through. This is how toolkit looks layer cleanly. [sl211]
- Fixtures not ticked keep running the Autoloop. To force one dark, include it at intensity 0. [slx]
- **Fades:** up to 30 s, for intensity, color and position. Attributes, strobe and movement snap. [sl211]
- **Active Static Looks pane:** reorder, mute, clear. Right-click to copy and paste looks. [sl211]
- **MIDI mapping:** right-click a control and move the hardware control. Custom mappings get no feedback LEDs. [midimap] [midifb]

## Fixture profiles
- **Color wheel:** set a range per color, then link the wheel in the Color Wheel attribute's "Wheel" column. The KB doesn't say how SoundSwitch picks a slot. [fmmh] [fmwheel]
- **Shutter:** a Strobe attribute with "Shutter Closed", "Shutter Strobe" and "Shutter Open" entries. This matters for the Vortex's closed shutter (Job V1). [fmmh]
- **Multi-cell fixtures:** the master dimmer and strobe must sit in a cell named exactly "MASTER". [fmpdf]
- **Smoke and haze:** driven through Attribute Cues. [fixtures]
- **Update Fixtures resetting names and groups:** no KB article covers it. We saw it ourselves: `session-log.md` 2026-10-06 and 2026-10-20.

## Strobe panel (the Shocker)
- Strobe is its own track: select a range, then Strobe (Shift+S) with a start rate and an end rate. [strobe]
- Effect fixtures "depend heavily on Attribute Cues". [fnr]
- The KB says nothing about blinders or strobe panels.
- (inferred) Why the Shocker does nothing in our Autoloops: it only fires where a loop has a Strobe block (or the STROBE button / Loop Auto Strobe triggers it), and only with its intensity above 0. Check its profile for Dimmer + Strobe with Shutter entries, and check the loops for Strobe blocks on its track.

## macOS, DMX and guest DJs
- macOS 27 is supported as of 2.11. The KB advises turning off automatic macOS updates. [mac27]
- **Connection fixes:** Local Network access for both apps, Full Disk Access, and firewall allow rules. [serext] [vdjts]
- **Virtual DJ** can link over IP from the DJ's own laptop (VDJ 2020+). Set OS2L to YES and SoundSwitch to Auto Connect. [vdjts] [vdjip]
- **rekordbox:** needs the Creative or Professional plan, then Preferences > Extensions > Lighting. [rb]
- **Wireless DMX:** wired is preferred. Test a link with the color overrides. [wireless]
- **Saving:** Save Project saves the venue, fixtures, Autoloops, Static Looks and cues. Save Lightshow saves scripts. [saving]

## Contradictions in the KB
- **Bank size:** 4 x 8 (old intro) vs 4 x 32 (2.9+). Ours is 4 x 32.
- **Export to Control One:** "fixture and Autoloop data" in one article vs "venue info, auto-loops, and static looks" in another.
- **Group buttons:** the guide's callout and the printed labels disagree on which is 1/3 and which is 2/4.

## Sources
[link]: https://support.soundswitch.com/en/support/solutions/articles/69000847102
[standalone]: https://support.soundswitch.com/en/support/solutions/articles/69000847411
[ui29]: https://support.soundswitch.com/en/support/solutions/articles/69000858488
[pdl]: https://support.soundswitch.com/en/support/solutions/articles/69000881392
[bpm]: https://support.soundswitch.com/en/support/solutions/articles/69000858486
[band]: https://support.soundswitch.com/en/support/solutions/articles/69000859725
[bpmaudio]: https://support.soundswitch.com/en/support/solutions/articles/69000870082
[midisync]: https://support.soundswitch.com/en/support/solutions/articles/69000847415
[compat]: https://support.soundswitch.com/en/support/solutions/articles/69000847104
[c1pdf]: https://cdn.inmusicbrands.com/soundswitch/files/User%20Guide%20Control%20One.pdf
[c1faq]: https://support.soundswitch.com/en/support/solutions/articles/69000847095
[c1fw]: https://support.soundswitch.com/en/support/solutions/articles/69000844241
[c1exp]: https://support.soundswitch.com/en/support/solutions/articles/69000859408
[omni]: https://support.soundswitch.com/en/support/solutions/articles/69000876803
[univ]: https://support.soundswitch.com/en/support/solutions/articles/69000847600
[alx]: https://support.soundswitch.com/en/support/solutions/articles/69000847100
[al29]: https://support.soundswitch.com/en/support/solutions/articles/69000858487
[ascript]: https://support.soundswitch.com/en/support/solutions/articles/69000844240
[new28]: https://support.soundswitch.com/en/support/solutions/articles/69000843903
[attr]: https://support.soundswitch.com/en/support/solutions/articles/69000828942
[fxgen]: https://support.soundswitch.com/en/support/solutions/articles/69000847595
[shapes]: https://support.soundswitch.com/en/support/solutions/articles/69000847396
[ctrl]: https://support.soundswitch.com/en/support/solutions/articles/69000847597
[keys]: https://support.soundswitch.com/en/support/solutions/articles/69000847406
[sl211]: https://support.soundswitch.com/en/support/solutions/articles/69000881393
[slx]: https://support.soundswitch.com/en/support/solutions/articles/69000863339
[midimap]: https://support.soundswitch.com/en/support/solutions/articles/69000847101
[midifb]: https://support.soundswitch.com/en/support/solutions/articles/69000847096
[fmmh]: https://support.soundswitch.com/en/support/solutions/articles/69000844508
[fmwheel]: https://support.soundswitch.com/en/support/solutions/articles/69000844589
[fmpdf]: https://cdn.inmusicbrands.com//soundswitch/FixtureManager/files/Fixture_Manager_Manual.pdf
[fixtures]: https://support.soundswitch.com/en/support/solutions/articles/69000844238
[strobe]: https://support.soundswitch.com/en/support/solutions/articles/69000847583
[fnr]: https://support.soundswitch.com/en/support/solutions/articles/69000848635
[mac27]: https://support.soundswitch.com/en/support/solutions/articles/69000883511
[serext]: https://support.soundswitch.com/en/support/solutions/articles/69000844855
[vdjts]: https://support.soundswitch.com/en/support/solutions/articles/69000843900
[vdjip]: https://support.soundswitch.com/en/support/solutions/articles/69000828941
[rb]: https://support.soundswitch.com/en/support/solutions/articles/69000881391
[wireless]: https://support.soundswitch.com/en/support/solutions/articles/69000865489
[saving]: https://support.soundswitch.com/en/support/solutions/articles/69000853039
