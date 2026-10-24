# Autoscript for Autoloops (SoundSwitch 2.7+)

Researched 2026-10-07 night: web search plus opening the dialog in SoundSwitch 2.11. The web has very little beyond the official article, so most of this comes from the app itself.

## How to run it (official article)
1. Edit mode > press **A** (Autoloop panel) > pick the bank (click its name) > double-click a slot. A new Autoloop can be 16, 32, 64 or 128 bars.
2. Click **AUTO** in the toolbar. The "Automation Settings" dialog opens.
3. Pick an Autoscript preset, choose which Position Cues and Attribute Cues to use and in what order, then **Apply**.
4. "Keep this dialog open" lets you re-apply (handy for the Random presets) until you like the result.

## The dialog (seen in 2.11)
- **Preset dropdown** (starts on "Base Styles"). The list: Base Styles, Dynamic Autoloop 1-6, Dance Autoloop 1-2, Random Color Autoloop 1-2. **Save as Preset** (bottom left) stores your own.
- **Checkboxes:** High Energy Pulse (on, greyed for Autoloops), Adaptive (Low BPM).
- **Knobs:**
  - **Base Intensity** (0% in Base Styles). This is the floor level the lights never drop below. **Raising it is the direct fix for "about 50% brighter".**
  - **Pulse Intensity** (100%). How hard the pulses hit.
  - Bridge Intensity (50%, greyed for Autoloops, since loops only have Main sections).
  - **Movement Speed**, **Color Change Speed**, **Effect Speed** (Slow to Fast). **Color Change Speed at Slow** matches Tony's "slow color changes" rule.
- **Color Scheme:** Primary / Secondary / Tertiary / Highlight swatches, with a **Custom Colors** checkbox. This is how to give an autoscripted loop a coordinated palette instead of random colors.
- **Effects:** Apply Movement, Apply Strobe (both on by default). Untick Apply Strobe to keep the Shocker out; untick Apply Movement to hold movers still on their positions.
- **Positions table:** one row per named position, with columns Intro / Main 1 / Main 2 / Bridge / Middle / Outro. Only **Main 1 and Main 2** are active for Autoloops. The number is the order the position is used in; **0 = not used** (Base Styles has every position at 0). The **R** under each column randomizes the order. **Change & Hold** checkbox under the list.
  - Leave 841 Logo, DJ Booth and Tiny Ball at 0: they only aim some lights.
- **Attribute Cues table:** same idea, Gobo Change 1-3, Custom Cue 1-5, smoke, numbered 1-8 by default.
- **Fixture categories matter:** the presets treat Wash Primary / Secondary / Tertiary, Mover Primary / Secondary / Tertiary, Spot, Strobe and so on differently. Ours are set on the DMX page (see `rig.md`). The article suggests splitting similar lights across Primary and Secondary to get call-and-answer between them.

## What users say (Engine DJ forum)
- Autoscript gets "80% of the result with 20% of the effort". Hand edits close the gap. Editing a full bank by hand took one user 40-50 minutes.
- Several users autoscript first, then save their own presets per genre. That took weeks, but they called it worth it.
- Known bug (confirmed by support): Autoscript can use positions you didn't pick, including ones set to 0, so a special-purpose position (our 841 Logo, DJ Booth) can show up mid-song. Saved presets can also lose their positions and attributes. Keep backups of presets that work.
- One user organizes banks by energy: slow/calm, hectic, fast strobes for techno, special/beam effects.

## How it fits Tony's rules
- Autoscript is a fast way to rough in a loop, then hand-edit: set Custom Colors to the look's palette, Color Change Speed Slow, Base Intensity up (40-60%), Apply Strobe off except on peak looks, and only the floor positions turned on. Then hand-edit: take the Pocket Beam out except for tiny-ball hits, add zero overrides for darkness, add the prism and gobo cues.
- **Gotcha (2026-10-07, about 21:30):** SoundSwitch froze while the preset dropdown was open, after scrolling the list with the mouse wheel. Pick presets with single clicks; don't scroll that list. Save before opening the dialog.

## Sources
- [SoundSwitch: How to Autoscript Autoloops](https://support.soundswitch.com/en/support/solutions/articles/69000844240-soundswitch-how-to-autoscript-autoloops)
- [Engine DJ forum: What bothers me most about SoundSwitch](https://community.enginedj.com/t/what-bothers-me-most-about-soundswitch/67266)
- [Engine DJ forum: Some questions about SoundSwitch](https://community.enginedj.com/t/some-questions-about-soundswitch/62406)
- [SoundSwitch 2.9 announcement (128 Autoloops, reorder, duplicate, populate)](https://news.hummingbirdmedia.com/lighting-control-software-soundswitch-announces-version-29-with-auto-bpm-detection-and-enhanced-autoloop-features)
- [bonedo: SoundSwitch 2.8 (phrase editing, Autoscript mixing, batch scripting)](https://www.bonedo.de/artikel/soundswitch-2-8-lighting-software-bringt-phrasenbearbeitung-verbessertes-batch-scripting-und-neue-styles/)
- [Mixdown: SoundSwitch 2.11 (Static Looks overhaul, rekordbox)](https://mixdownmag.com.au/news/soundswitch-announce-soundswitch-2-11/)

## Gotchas (2026-10-23)
- **The dialog resets** to Base Styles with every position and cue at 0 each time it opens. Re-enter everything; it isn't remembered (contrary to the 10-07 note).
- **Knobs follow the mouse angle**, not a vertical drag: drag from the knob's centre towards a clock position (7 o'clock = 0%, 12 = 50%, 5 o'clock = ~99%). A scroll-wheel notch moves it 1%.
- **Re-applying deletes hand-placed attribute cues** on the Main Track. Autoscript only places Main 1 cues in a 16-bar Autoloop (bars 1-8); Main 2 cues have to be dragged on by hand.
- The cue table scrolls with the wheel; check which row a click lands on, since the scroll amount varies.

## Gotchas (2026-10-24, filling 95 slots by script)
- **Pick the preset with the keyboard.** The preset list scrolls to the current preset, so clicking a row by position lands on the wrong one, and the wheel froze the app before. Open the list, press Up 12 times and Return (that lands on Base Styles), then open it again and press Down N times and Return. Order below Base Styles: Dynamic 1-6, Dance 1, Dance 2, Random Color 1, Random Color 2.
- **"Cue data missing" popup** (One or more cue selections have not been specified) appears on Apply when a Main 2 cue column is empty. Tick "Don't show again" and choose "Continue anyway". That setting is lost if SoundSwitch is force-quit.
- **Apply rewrites a hand-built loop's fixture tracks.** Checked by eye on R2 1 Deep Blue: its hand-made blocks were gone after Apply. Not checked track by track.
- The dialog is a separate window and can be dragged by its title bar; the colour picker opens relative to it (+349, +228).
- SoundSwitch froze once (2026-10-24 00:10) with the dialog open after a few hundred scripted clicks. Save after every slot.

