# Facts 2: Autoloops, from the official SoundSwitch YouTube videos

Source: `/Users/tonyw/Dropbox/SoundSwitch/youtube-captions/txt/` (95 auto-caption transcripts, read 2026-10-21). All 13 requested videos were read in full. All 95 were grepped for: autoloop, autoscript, preset, bank, exclusive, override, auto-strobe, attribute cue, position cue, phrase, silence, blackout, pause, plus main/master/group/fixture track, category, primary/secondary/tertiary, smoke, Link, tap. Other videos with relevant hits were read in full and are cited too.

- **STATED** = the video says or shows it (paraphrased here). **INFERRED** = my conclusion from what the videos say. It is not verified on Tony's rig.
- Captions are machine-made: "Master Track" and "main track" mean the same thing, "the platypus" is the platter, and so on.
- Each fact names its video and year. Videos from 2016-2021 show older versions (Tony runs 2.11). Version drift is flagged where it matters.

---

## Short answers

**1. How Autoloops address fixtures, and why the lights "move as one"**
- An Autoloop has three layers of tracks:
  - the **Main (Master) Track**, which drives every fixture in the venue;
  - **Group tracks**, which drive the fixtures in one workspace group;
  - **Fixture tracks**, which override the Main Track for one fixture.
- The Main Track content is identical in every venue. Group and fixture-track content has to be built for each venue.
- **Fixture categories** (Wash / Mover / Spot / Multi-cell / Strobe-Blinder, each Primary / Secondary (/Tertiary)) are read by **Autoscript only**. The videos never say they change how a hand-built or stock loop plays.
- **Control Groups 1-4** (2.3+) are intensity faders, in Performance mode and on the Control One touch strip. They are not an addressing layer.
- **Why "move as one":**
  - The stock Autoloops (and any loop built only on the Main Track) have no fixture-track content (STATED, 2023). Fixture-track effects ship only for the GigBar Move demo venue. A custom venue has to add its own (STATED, 2021).
  - So every light gets the same intensity, color and strobe at the same moment. Every mover jumps to its position cue on the same beat. A Main-Track movement shape moves all movers in step (INFERRED from STATED mechanics).
- **Why lights sit idle:**
  - Movers don't move until the Position Cues hold pan/tilt for that venue.
  - Gobo, prism, derby and similar features change only through Attribute Cues.
  - Both are set per venue (STATED). (Applying this to Tony's "half the lights aren't used" is INFERRED.)

**2. How to make Autoloops dynamic**
- **The official fix is to run Autoscript on the Autoloop** (2023 video, 2.7+).
  - It spreads effects across the fixture tracks based on the venue's actual fixtures and their categories.
  - Keep the Advanced dialog open, then try presets and re-apply until it looks right.
- **Presets:** Dynamic (the default), House & Techno, smooth, trap, electro, and others. The (i) icon explains what each preset does per fixture category and per section.
- **Knobs:**
  - Base Intensity: the floor, so lights stop dropping to 0.
  - Pulse Intensity: the peak.
  - Bridge Intensity.
  - Movement Speed: how often position cues fire.
  - Color Change Speed: how often colors change.
  - Effect Speed: how often chases are placed.
  - Plus custom colors (Primary / Secondary / Tertiary).
- **Cues:** you pick which Position and Attribute Cues are used, and their order, per section (Intro / Main 1 / Main 2 / Bridge / Middle / Outro), or randomize them.
  - **Change & Hold** on = hold, then snap to the next position. Off = a slow glide.
- **Categories:** put similar lights in different categories (Wash Primary vs Wash Secondary) and they get different effects. Change a category and re-run to compare.
- **Hand tools that break "move as one":**
  - chases on group tracks, or across selected fixture tracks;
  - fixture-track color overrides (a contrasting palette on some lights);
  - **Position overrides** per mover (a different shape or position from the Main Track);
  - **Random Position** and **Position Chase** effects, which put an **offset** between lights;
  - Change & Hold;
  - an intensity or strobe override on single fixtures.
- **Phrase editing** (2023) is shown on tracks, not Autoloops. It relabels sections, alternates Main 1 and Main 2, protects sections, and mixes presets by section.

**3. Playback**
- **Banks:**
  - 2019: 4 banks of 8 (32 loops).
  - Since 2.9: 4 banks of 32 (128 loops).
  - Each bank has an autoplay switch. Turn it off for drop, strobe or special banks and launch those by hand or MIDI.
  - Picking one bank plays only that bank. "Play all banks" goes back to all of them.
- **Order and controls:** Sequential or Random. Next / Previous. Repeat (holds the current loop to the end of the track).
- **Autoloop Override** ignores scripted tracks (MIDI-mappable, and in Preferences > Performance Mode). Since 2.9 you can also fire any Autoloop over a scripted track.
- **Loop Auto-Strobe** strobes when the DJ uses a loop or loop roll of half a beat or less. It's a DJ-software feature: no DJ loops, no auto-strobe (INFERRED).
- **"Exclusive bank" is in no video.** It comes only from the KB (see `notes/soundswitch-kb.md`).
- Strobe fixtures:
  - The built-in strobes on all-in-one bars are driven by Attribute Cues.
  - Other lights strobe from the strobe track.
  - The videos never say what Autoscript does with a "Strobe/Blinder" category fixture.

**4. Tempo and idle**
- **BPM Detection** (2.9, 2024) has two silence options for when the audio drops below the threshold line:
  - **Blackout** blacks the lights out;
  - **Pause Autoloops** pauses the show.
  - The threshold only sets that behavior. Detection runs at all levels. Set the line just above the room noise.
  - The video never says what happens with neither box ticked.
- **Pause behavior:** pausing in Performance mode "freezes the lights in a particular state" (2021). The same happens when a deck is paused in DJ software. That fits Tony's 10-20 sighting of a lit held frame (INFERRED).
- **Link** (2018 videos): turn Link on in both apps, on the same computer or the same network. Autoloops then follow that app's tempo, and Autoloops, Static Looks and overrides can still be launched.
- **Standalone / Control One:** Shift+Link starts Autoloops at 120 BPM. Tap BPM to set the tempo. Shift+Play/Pause resets the phrase to beat 1.
- **MIDI Clock:** needs Cue to start and Beat Shift to fix the phase.
- None of the videos says what an Autoloop does when Link drops or the tempo stops.

**5. SoundSwitch's recommended workflow**
1. Get the beatgrids right in the DJ software.
2. Patch the venue in sensible groups (left / center / right). Name the fixtures and check with a color override.
3. Set the fixture categories on purpose.
4. Fill in the Position Cues. Movers should always point outward from the booth, never behind it.
5. Fill in the Attribute Cues.
6. Autoscript the Autoloops with the dialog kept open: try presets, tune the knobs and cue order, re-apply.
7. Hand-edit: Main Track for the broad strokes, group tracks for chases, fixture tracks for contrast and overrides.
8. Build special-purpose banks for drops, breakdowns, intros and strobe-heavy looks. Exclude them from autoplay and MIDI-map them.
9. Copy tracks between loops selectively.

---

## Detailed facts

### Q1. How Autoloops address fixtures

| # | Fact | Type | Source |
|---|---|---|---|
| 1.1 | The Main Track sits at the bottom of the workspace and controls all of the lights. Intensity or color placed there shows on every fixture. | STATED | [Advanced Features (2021) @02:56](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=176) |
| 1.2 | Color put on a group track is followed by every light in that group. Color put on a fixture track changes only that fixture, overriding the Main Track. The video says this layering is what makes color chases possible. | STATED | [Advanced Features (2021) @03:29](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=209) |
| 1.3 | Intensity (an "intensity override"), strobe and movement can each be overridden per fixture. The example is one GigBar mover that strobes and gets its own Position Cue. | STATED | [Advanced Features (2021) @04:33](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=273) |
| 1.4 | Main Track content is the same in every venue. Opening the same Autoloop under different venues shows identical Main Track data, so a new rig gets a basic show with no rescripting. | STATED | [Advanced Features (2021) @01:07](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=67), [@01:43](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=103); also [Scripting Session 1 (2016) @08:12](https://www.youtube.com/watch?v=EETBfocNxOY&t=492) |
| 1.5 | The shipped Autoloops have fixture-track effects for the GigBar Move venue only. For your own venue, you have to add chases or color changes to the fixture tracks yourself. | STATED | [Autoloops Explained (2021) @03:09](https://www.youtube.com/watch?v=dwe6g-qczjI&t=189), [@03:39](https://www.youtube.com/watch?v=dwe6g-qczjI&t=219) |
| 1.6 | The stock Autoloops used to have effects in the Main Track only. A basic Bank 4 loop is shown with nothing on any fixture track. | STATED | [Autoloop AutoScripting (2023) @00:32](https://www.youtube.com/watch?v=5alSfsuWigQ&t=32), [@01:04](https://www.youtube.com/watch?v=5alSfsuWigQ&t=64) |
| 1.7 | **Why "move as one":** a loop with only Main Track content gives every fixture the same intensity, color and strobe at the same moment. Position cues in the Main Track fire for all movers on the same beat. Each mover goes to its own stored pan/tilt for that named position, but they all change together. | INFERRED (from 1.1, 1.5, 1.6, 1.10) | - |
| 1.8 | A movement shape on the Main Track (figure-8) is followed by every mover that isn't overridden. To get different shapes, the outer movers got a Position override with a circle, while the GigBar movers kept the Main Track figure-8. | STATED | [Movement & Attribute Cues (2021) @09:05](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=545), [@09:35](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=575) |
| 1.9 | A Position override makes a light stop following the Main Track. You create one by selecting in a mover's position track, right-clicking, and choosing create position override. | STATED | [Advanced Chase Effects (2017) @01:26](https://www.youtube.com/watch?v=pxU4nqV5ebw&t=86) |
| 1.10 | Position Cues are named positions. Each mover's pan/tilt is set inside the cue (one mover at a time or several together). Pressing Apply updates every cue in the Main Track and in every Autoloop and script, so nothing needs rescripting. | STATED | [AutoScripting Explained (2021) @08:53](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=533), [@09:29](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=569); [Movement & Attribute Cues (2021) @05:55](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=355) |
| 1.11 | Movers won't move until the Position Cues have pan/tilt set. | STATED | [Autoloops Explained (2021) @06:50](https://www.youtube.com/watch?v=dwe6g-qczjI&t=410); [Getting Started (2021) @16:22](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=982) |
| 1.12 | SoundSwitch splits channels into "standard" ones (intensity, color, strobe, pan/tilt), which the control tracks drive, and everything else (gobo, prism, laser, smoke and so on), which only Attribute Cues drive. | STATED | [Movement & Attribute Cues (2021) @00:38](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=38) |
| 1.13 | Attribute Cue flags sit in the Main Track. The settings inside a cue are stored per fixture, and editing a cue updates every flag that uses it. | STATED | [Movement & Attribute Cues (2021) @07:28](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=448); [Getting Started (2021) @15:12](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=912) |
| 1.14 | **Why lights sit idle:** a fixture whose main appeal is gobo, prism or rotation (scanners, the Vortex) looks static unless the loop's Attribute Cues hold values for it. A mover looks static unless Position Cues or movement are present. | INFERRED (from 1.11-1.13) | - |
| 1.15 | Fixture categories are set on the DMX map. "Fixture categories are used by the automation" to apply different effects. The example is outer top washes as Wash Primary, bottom washes as Wash Secondary and the GigBar as Mover Primary. | STATED | [AutoScripting Explained (2021) @04:56](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=296), [@05:28](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=328), [@05:59](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=359) |
| 1.16 | Category choices named in the videos: Wash Light, Spotlight, Multi-cell, Strobe or Blinder (with Wash Primary suggested for most cases), and Mover Primary. | STATED | [GigBar 2 Tutorial (2020) @00:39](https://www.youtube.com/watch?v=tUO9Tp234zk&t=39); [AutoScripting Explained (2021) @05:59](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=359) |
| 1.17 | The videos tie categories only to Autoscript. Nothing says a category changes how a hand-built or stock Autoloop plays back. | INFERRED (absence) | - |
| 1.18 | **Control Groups 1-4** (new in 2.3) are set in the DMX map and drive the group intensity faders in Performance mode. They can work per group or per fixture. | STATED | [What's New in 2.3 (2021) @02:48](https://www.youtube.com/watch?v=HSue8aJVn8c&t=168), [@03:22](https://www.youtube.com/watch?v=HSue8aJVn8c&t=202) |
| 1.19 | On the Control One the touch strip scales Autoloop or scripted intensity, or Group 1 to Group 4 intensity. | STATED | [Getting Started with the Control One (2021) @03:20](https://www.youtube.com/watch?v=eHgkltVdG-I&t=200); [Control One x Serato (2021) @07:11](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=431) |
| 1.20 | Control Groups are a live dimming layer, not something an Autoloop sends to. The workspace "fixture groups" (group tracks) are a separate concept. | INFERRED | - |
| 1.21 | Workspace fixture groups are made with "insert a fixture group". The example groups lights by side of the booth (left / center / right). An all-in-one fixture gets its own group automatically. | STATED | [AutoScripting Explained (2021) @01:40](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=100), [@02:10](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=130), [@02:40](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=160) |
| 1.22 | A chase dropped on a group track runs across the fixtures in that group. A chase dropped on a selection of groups and fixtures asks whether to run it within each group or across the selected fixtures. | STATED | [Effects Generator Pt 1 (2016) @00:41](https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=41), [@01:20](https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=80), [@01:51](https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=111) |

### Q2. Making Autoloops dynamic

**Autoscript on Autoloops**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.1 | Autoscript can now be applied to Autoloops. It generates more dynamic loops and "takes into consideration the different lights you have". | STATED | [Autoloop AutoScripting (2023) @00:32](https://www.youtube.com/watch?v=5alSfsuWigQ&t=32) |
| 2.2 | Running Autoscript with the Dynamic preset on a Main-Track-only loop places a wider range of effects across the fixtures in the venue. SoundSwitch calls it a fast way to improve the shipped loops. | STATED | [Autoloop AutoScripting (2023) @01:36](https://www.youtube.com/watch?v=5alSfsuWigQ&t=96), [@02:37](https://www.youtube.com/watch?v=5alSfsuWigQ&t=157) |
| 2.3 | Recommended loop: open Advanced, keep the dialog open, try presets, and apply again until you like it. You can also adjust movement and color change speed, slow the effects, and randomize the Position and Attribute Cues. | STATED | [Autoloop AutoScripting (2023) @02:07](https://www.youtube.com/watch?v=5alSfsuWigQ&t=127); same advice for tracks in [AutoScripting Explained (2021) @12:44](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=764) |
| 2.4 | Presets named: Dynamic (the one picked in every demo), House and Techno, and others "smooth or designed for trap and electro". | STATED | [Getting Started (2021) @18:00](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=1080); [AutoScripting Explained (2021) @06:34](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=394), [@11:42](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=702) |
| 2.5 | The (i) icon next to a preset lists what it applies to the lights, to each fixture category and to each section of the track. | STATED | [AutoScripting Explained (2021) @12:14](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=734) |
| 2.6 | 2.2 introduced styles. You can start from a base style, add your own settings and save the result as a preset. | STATED | [SoundSwitch 2.2 (2020) @00:05](https://www.youtube.com/watch?v=Wis8O1gTWP8&t=5) |
| 2.7 | 2.3 added a basic menu for picking a preset without opening Advanced, and made automation apply "more effects based on the fixture category". | STATED | [What's New in 2.3 (2021) @03:52](https://www.youtube.com/watch?v=HSue8aJVn8c&t=232), [@04:26](https://www.youtube.com/watch?v=HSue8aJVn8c&t=266) |

**Automation dialog controls**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.8 | Knobs: base intensity, pulse intensity, bridge intensity, movement speed, color change speed and effect speed. There are also custom colors and a choice of which Position and Attribute Cues are placed, in what order and in which section. | STATED | [AutoScripting Explained (2021) @12:14](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=734) |
| 2.9 | Base intensity above 0 means the lights stop going all the way down. At 0 they pulse from 0 to 100%. A pulse intensity of 47 caps the pulses at 47%. | STATED | [AutoScripting Explained (2021) @12:44](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=764), [@13:18](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=798) |
| 2.10 | Movement speed sets how often Position Cues are applied. Color change speed sets how often colors change. Effect speed sets how often, or how quickly, chases are applied to fixtures. A higher effect speed places chases much more often. | STATED | [AutoScripting Explained (2021) @13:18](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=798), [@13:51](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=831) |
| 2.11 | Position order is chosen per section (intro, main 1, main 2, bridge, middle, outro). Example: Stage Left first and Stage Right second during the intro. The order can be L-R-R-L or randomized. | STATED | [AutoScripting Explained (2021) @13:51](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=831), [@14:22](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=862) |
| 2.12 | With **Change & Hold** on, lights hold a point and then change quickly to the next. With it off, they move slowly from one position to the next. | STATED | [AutoScripting Explained (2021) @14:22](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=862), [@14:56](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=896) |
| 2.13 | The color options are Primary, Secondary and Tertiary custom colors. Attribute Cues are chosen per section, and On and Off cues should be set in the right order. | STATED | [GigBar 2 Tutorial (2020) @07:12](https://www.youtube.com/watch?v=tUO9Tp234zk&t=432) |
| 2.14 | No video says how the Primary / Secondary / Tertiary colors map to fixtures (by category or otherwise). | INFERRED (gap) | - |
| 2.15 | Cue folders (new in 2.1) can be added to the automation's "used" list, which adds every cue in the folder. | STATED | [SoundSwitch 2.1 (2019) @01:41](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=101), [@02:15](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=135) |

**Categories**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.16 | Lights categorized differently get different effects. After autoscripting, the Wash Primary and Wash Secondary fixtures in one group carry different effects. SoundSwitch suggests experimenting: change a category at any time and look at the result. | STATED | [AutoScripting Explained (2021) @05:28](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=328), [@05:59](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=359), [@07:48](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=468) |
| 2.17 | Changing a fixture's category and rescripting changes the effects on that fixture. | STATED | [What's New in 2.3 (2021) @04:26](https://www.youtube.com/watch?v=HSue8aJVn8c&t=266) |
| 2.18 | **For Tony:** putting matching fixtures in different categories (one Tripar side Wash Primary, the other Wash Secondary; one scan pair Mover Primary, the other Mover Secondary) is the videos' main lever against "move as one" under Autoscript. Two Primary/Secondary pairs give more variety than four identical categories. | INFERRED | - |

**What the analysis does by section (tracks; 2020)**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.19 | The analysis finds intros and outros, Main 1 and Main 2, and bridge and middle sections, and gives each one unique effects. Drops get intensity, color and strobe. Build-ups and breakdowns get strobe, color transitions and movement. | STATED | [SoundSwitch 2.2 (2020) @00:05](https://www.youtube.com/watch?v=Wis8O1gTWP8&t=5), [@00:38](https://www.youtube.com/watch?v=Wis8O1gTWP8&t=38) |
| 2.20 | Automation can place chase effects, intensity overrides and Attribute Cues on specific fixtures. | STATED | [SoundSwitch 2.2 (2020) @01:12](https://www.youtube.com/watch?v=Wis8O1gTWP8&t=72) |
| 2.21 | No video says which sections an Autoloop is treated as. (The app dialog in 2.11 shows only Main 1 and Main 2 active for Autoloops, per `notes/autoscript.md`. That is not from a video.) | gap | - |

**Phrase editing (tracks; 2023)**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.22 | Autoscript splits a track into intro, outro, middle, bridge, Main 1 and Main 2 using the beatgrid and the energy. Main 1 and Main 2 stand for verse and chorus but are interchangeable. Each phrase type gets its own effects. | STATED | [Autoscript Phrase Editing (2023) @00:02](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=2), [@00:32](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=32) |
| 2.23 | For variety: unlock the phrase grid and relabel every second Main 1 as Main 2. Sections can also be split, merged and renamed. | STATED | [Autoscript Phrase Editing (2023) @02:03](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=123) |
| 2.24 | "Disable scripting" protects sections. Refresh then re-autoscripts only the enabled sections, possibly with a different preset, which mixes presets by section. Sections can be resized with bar or beat snapping, or none. Enable all, disable all and invert are available. Lock the grid when done. | STATED | [Autoscript Phrase Editing (2023) @02:34](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=154), [@03:04](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=184), [@03:34](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=214), [@04:06](https://www.youtube.com/watch?v=m_iJS6RE01Q&t=246) |
| 2.25 | The video shows phrase editing on a music track only. Whether Autoloops have a phrase grid is not shown. | gap | - |

**Hand-editing techniques that de-sync the lights**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.26 | A forward chase on a group track, pulsing every quarter beat, makes a chill loop's lights chase. | STATED | [Autoloops Explained (2021) @03:39](https://www.youtube.com/watch?v=dwe6g-qczjI&t=219) |
| 2.27 | Chases go inside each group (each group of Freedom Sticks chases on its own), then an overall chase runs across all of the selected tracks for the second half of the drop. | STATED | [Custom Scripted Tracks Pt 4 (2018) @01:59](https://www.youtube.com/watch?v=1p7SDBxizKo&t=119); [Pt 1 (2018) @02:18](https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=138) |
| 2.28 | Put one color scheme on the Main Track (warm reds, oranges and yellows) and a contrasting one (blues) on some of the other fixtures. | STATED | [Scripting Session 1 (2016) @03:32](https://www.youtube.com/watch?v=EETBfocNxOY&t=212), [@04:02](https://www.youtube.com/watch?v=EETBfocNxOY&t=242) |
| 2.29 | A fixture-track color override gives one mover a different color. Copy and paste it to the other mover. | STATED | [Movement & Attribute Cues (2021) @08:00](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=480), [@08:33](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=513) |
| 2.30 | Filter the workspace to movers only and select their fixture tracks. Then use any of three movement effects. | STATED | [Movement & Attribute Cues (2021) @10:06](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=606) |
| | - **Random Position effect** (cues every 2 bars): positions are randomized across those fixtures. | STATED | [@10:40](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=640) |
| | - **Change & Hold** effect (every bar). | STATED | [@10:40](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=640) |
| | - **Position Chase** through Stage Left, Stage Right and Dance Floor every half bar, which "applies an offset" between the lights. | STATED | [@11:16](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=676), [@11:46](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=706) |
| 2.31 | Position chase by hand: give each mover a Position override, then place cues in reverse order so a light changes and then holds. Color chase: drag Color Chase onto a selection across fixtures. Pulse chase: Forward Chase, timed every quarter beat. | STATED | [Advanced Chase Effects (2017) @01:26](https://www.youtube.com/watch?v=pxU4nqV5ebw&t=86), [@01:59](https://www.youtube.com/watch?v=pxU4nqV5ebw&t=119), [@02:33](https://www.youtube.com/watch?v=pxU4nqV5ebw&t=153) |
| 2.32 | A random intensity effect on the Main Track gives a flicker. | STATED | [Effects Generator Pt 1 (2016) @00:41](https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=41) |
| 2.33 | Hue color adjust recolors a whole Autoloop or a selection with one slider. Unlink turns the colors into color transitions. | STATED | [Advanced Features (2021) @06:44](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=404), [@07:14](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=434) |

**Movement**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.34 | A movement effect (figure-8, circle and others) has a speed and size that can change from the start to the end of the selection. Placing a Position Cue makes the shape run around that position. | STATED | [Movement & Attribute Cues (2021) @06:26](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=386), [@06:56](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=416); [Quick Tips: Movement Shape FX (2019) @00:01](https://www.youtube.com/watch?v=Gk1GfC1OQlM&t=1) (adds direction) |
| 2.35 | A figure-8 can be made to speed up over time. | STATED | [Autoloops Explained (2021) @06:20](https://www.youtube.com/watch?v=dwe6g-qczjI&t=380) |
| 2.36 | Space position moves far apart for smooth transitions. | STATED | [Scripting Session 1 (2016) @07:39](https://www.youtube.com/watch?v=EETBfocNxOY&t=459) |

**Strobe**

| # | Fact | Type | Source |
|---|---|---|---|
| 2.37 | A strobe effect is a block in the strobe track with a start and an end strobe intensity. | STATED | [Editing Colors, Strobe & Overrides (2019) @00:37](https://www.youtube.com/watch?v=vjgRslXhxvk&t=37); [Movement & Attribute Cues (2021) @02:54](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=174) |
| 2.38 | Strobe can be overridden in group and fixture tracks. With the group's strobe at 0, that group doesn't strobe while a fixture track "will still strobe in time with the Master Track". The caption is ambiguous about which fixture that is. | STATED (wording ambiguous) | [Editing Colors, Strobe & Overrides (2019) @01:51](https://www.youtube.com/watch?v=vjgRslXhxvk&t=111) |

### Q3. Playback

| # | Fact | Type | Source |
|---|---|---|---|
| 3.1 | When a song with no script or Autoscript plays, Autoloops load automatically and sync to the DJ software's beatgrid. When one loop ends, SoundSwitch starts and syncs the next. | STATED | [Autoloops Explained (2019) @00:03](https://www.youtube.com/watch?v=fUVeC0Hs5fw&t=3), [@00:38](https://www.youtube.com/watch?v=fUVeC0Hs5fw&t=38) |
| 3.2 | **2019:** 32 Autoloops in 4 banks of 8. Each bank has a switch that includes it in or excludes it from autoplay. Playback is Random or Sequential, with an option to override scripted tracks. | STATED (old version) | [Autoloops Explained (2019) @01:12](https://www.youtube.com/watch?v=fUVeC0Hs5fw&t=72) |
| 3.3 | **2.9 (2024):** 128 Autoloops in 4 banks of 32. On upgrade the old 32 were spread across the 4 banks. "Populate" fills only empty slots with new defaults and leaves your own loops alone. Loops can be rearranged between banks and duplicated. | STATED | [SoundSwitch 2.9 x BPM Detection (2024) @04:03](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=243), [@04:33](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=273) |
| 3.4 | **2.9:** in Performance mode, Autoloops can be triggered at any time, including over scripted tracks. Visual feedback improved in the app and on the Control One. | STATED | [SoundSwitch 2.9 (2024) @05:03](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=303) |
| 3.5 | **2021:** picking one bank (e.g. "relaxed lights") means only that bank plays. Next and Previous step through the play order. **Repeat** keeps replaying the current loop to the end of the audio file. | STATED | [Autoloops Explained (2021) @09:36](https://www.youtube.com/watch?v=dwe6g-qczjI&t=576), [@10:06](https://www.youtube.com/watch?v=dwe6g-qczjI&t=606) |
| 3.6 | Override all scripted tracks with Autoloops only if you're sure the loops are what you want. Leave it off when scripted tracks should play. | STATED | [Autoloops Explained (2021) @10:06](https://www.youtube.com/watch?v=dwe6g-qczjI&t=606), [@10:38](https://www.youtube.com/watch?v=dwe6g-qczjI&t=638) |
| 3.7 | Sequential or random. "Play all banks" brings all banks back and randomizes their playback. | STATED | [Autoloops Explained (2021) @10:38](https://www.youtube.com/watch?v=dwe6g-qczjI&t=638) |
| 3.8 | Untick a bank's autoplay checkbox and its loops never play automatically. The suggested use is a bank of drop or effect loops, e.g. heavy strobe, that shouldn't fire at random mid-song. | STATED | [Autoloops Explained (2021) @11:09](https://www.youtube.com/watch?v=dwe6g-qczjI&t=669) |
| 3.9 | **2018:** a special-effects bank holds drop, breakdown and intro loops. Its autoplay toggle (top right of the bank) is turned off, and the loops are launched from MIDI pads (right-click to arm, then press the pad). | STATED | [Scripting Session: Autoloops and MIDI (2018) @00:03](https://www.youtube.com/watch?v=WpIH8pw1z84&t=3), [@02:53](https://www.youtube.com/watch?v=WpIH8pw1z84&t=173), [@03:57](https://www.youtube.com/watch?v=WpIH8pw1z84&t=237) |
| 3.10 | Autoloop Override (ignore scripted tracks, Autoloops only) can be MIDI-mapped (MIDI setup > Autoloops tab) or set in Preferences > Performance Mode. | STATED | [Quick Tips: Autoloop Overrides (2019) @00:02](https://www.youtube.com/watch?v=LF548RAwFag&t=2) |
| 3.11 | The Control One has an Autoloop override control that overrides scripted tracks. | STATED | [Getting Started with the Control One (2021) @01:38](https://www.youtube.com/watch?v=eHgkltVdG-I&t=98) |
| 3.12 | **Loop Auto-Strobe** (a Performance mode preference) strobes automatically when the DJ uses a loop or loop roll of half a beat or less. | STATED | [Quick Tips: Loop Auto-Strobe (2019) @00:02](https://www.youtube.com/watch?v=xTonfl6g3AM&t=2); [Getting Started (2021) @22:49](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=1369) |
| 3.13 | Loop Auto-Strobe depends on DJ-software loop data, so it does nothing under Link, BPM Detection or Standalone. | INFERRED | - |
| 3.14 | Control One: the pads play a single bank. Shift returns to playing all banks. The pad matrix toggles between Autoloops and Static Looks. A Static Look or Position override that is still active is shown "underneath" by the pad LEDs. | STATED | [Control One x Serato (2021) @05:33](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=333), [@06:08](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=368), [@06:39](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=399) |
| 3.15 | The Control One can store venue and Autoloop data on the device, so visiting DJs can plug in and play the house loops. | STATED | [Getting Started with the Control One (2021) @06:02](https://www.youtube.com/watch?v=eHgkltVdG-I&t=362) |
| 3.16 | Default banks in 2021: Bank 1 upbeat dance, Bank 2 upbeat but not dance, Banks 3-4 hip hop and chill. The defaults are "pretty basic": color, intensity, some movement, with Attribute Cues pre-placed. | STATED | [Getting Started (2021) @10:44](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=644), [@11:20](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=680) |
| 3.17 | 2.3 updated all the default Autoloops. Options > Reset Default Autoloops restores them. | STATED | [What's New in 2.3 (2021) @03:22](https://www.youtube.com/watch?v=HSue8aJVn8c&t=202) |
| 3.18 | Static Looks override whatever Autoloop is playing. Fixtures left out of a look keep following the Autoloop underneath. | STATED | [Static Looks Explained (2021) @02:07](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=127), [@05:46](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=346) |
| 3.19 | **Strobe fixtures:** an all-in-one bar's built-in strobes are set in an Attribute Cue. To strobe the other lights, use the strobe track. | STATED | [GigBar 2 Tutorial (2020) @02:20](https://www.youtube.com/watch?v=tUO9Tp234zk&t=140) |
| 3.20 | Attribute Cues can switch the GigBar's strobes on and off. | STATED | [Getting Started (2021) @15:48](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=948) |
| 3.21 | Strobe or Blinder is a category. | STATED | [GigBar 2 Tutorial (2020) @00:39](https://www.youtube.com/watch?v=tUO9Tp234zk&t=39) |
| 3.22 | No video says how Autoscript or Autoloops treat a Strobe/Blinder-category fixture. | gap | - |
| 3.23 | **"Exclusive bank":** no transcript out of 95 contains "exclusive". The long-press exclusive bank comes only from the KB. | gap | grep of all transcripts |

### Q4. Tempo and idle

| # | Fact | Type | Source |
|---|---|---|---|
| 4.1 | BPM Detection (2.9) listens to a sound card or internal mic and lets Autoloops run beat-synced to any live audio. A USB audio interface is the ideal source. | STATED | [SoundSwitch 2.9 x BPM Detection (2024) @00:01](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=1) |
| 4.2 | Settings are in Preferences > Tempo Detection: source, refresh rate (lower when the tempo changes often, higher for a steady house set) and BPM range. | STATED | [SoundSwitch 2.9 (2024) @01:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=62), [@01:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=92) |
| 4.3 | **Silence behavior:** two checkboxes decide what happens when the audio falls below the meter's threshold line. **Blackout** blacks out the lights. **Pause Autoloops** just pauses the light show. | STATED | [SoundSwitch 2.9 (2024) @01:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=92), [@02:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=122) |
| 4.4 | Detection runs at every volume. The threshold only triggers the blackout or pause. On an internal mic, set the line just above the room's ambient noise and below the music. It can be changed while the show runs. | STATED | [SoundSwitch 2.9 (2024) @02:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=152), [@03:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=182) |
| 4.5 | The video doesn't say how long the silence must last, or what happens when neither box is ticked. (The KB's "3 s" is not in the video.) | gap | - |
| 4.6 | To activate: Source selection menu (top left) > BPM Detection > toggle on. The detected BPM and the current beat of the 4-beat phrase show at the top left. | STATED | [SoundSwitch 2.9 (2024) @03:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=182) |
| 4.7 | To reset the phase to beat 1: Shift + Play/Pause on the Control One, or the Cue button on the Standalone tab. Color, strobe and other overrides and Static Looks still work on top. | STATED | [SoundSwitch 2.9 (2024) @03:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=182), [@03:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=212) |
| 4.8 | **Pause = freeze.** The Performance mode play/pause control is used "to freeze the lights in a particular state". | STATED | [Getting Started (2021) @04:46](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=286) |
| 4.9 | With DJ software, pausing a deck pauses its light show. | STATED | [Getting Started (2021) @20:46](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=1246) |
| 4.10 | Pulling the up-fader down dims that deck's lights. | STATED | [SoundSwitch X Virtual DJ (2021) @02:24](https://www.youtube.com/watch?v=pbON1Ce46OE&t=144) |
| 4.11 | Tony's 10-20 observation (steady amber, no look active) matches 4.8: a paused or stalled loop holds its last frame lit. For an unattended party, Blackout is the silence setting that fails dark. | INFERRED | - |
| 4.12 | **Link (2018):** turn Link on in Serato, Traktor or Live and in SoundSwitch, on separate computers on one network or on the same computer. SoundSwitch's BPM follows the other app's tempo changes. | STATED | [SoundSwitch x Ableton LINK x Serato DJ (2018) @00:09](https://www.youtube.com/watch?v=_udEdlyecGY&t=9); [x Traktor Pro 2 (2018) @00:04](https://www.youtube.com/watch?v=pvLHELfYkG8&t=4); [x Ableton Live (2018) @00:03](https://www.youtube.com/watch?v=rr5r24r6Ztw&t=3) |
| 4.13 | Under Link, SoundSwitch acts as a lighting controller: you launch Autoloops, Static Looks and MIDI overrides yourself while staying in sync. | STATED | [SoundSwitch x Ableton LINK x Serato DJ (2018) @00:42](https://www.youtube.com/watch?v=_udEdlyecGY&t=42) |
| 4.14 | No video says what happens when the Link peer stops or leaves. | gap | - |
| 4.15 | **Standalone (2019):** on the Standalone screen, the LINK button starts a show with no DJ input. Drag the BPM display, tap the BPM, or use the fine BPM knob. Cue and Beat-shift bring it back in phase. Autoloops launched from the screen are quantized to that BPM. | STATED (old UI) | [Standalone Mode (2019) @00:04](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=4), [@00:39](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=39), [@01:47](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=107) |
| 4.16 | **Control One standalone (2021):** Shift + the Link button starts Autoloops at 120 BPM. Tap BPM to match the music, and Shift + Play/Pause re-phrases to the downbeat. The BPM tap button doubles as the Link on/off control. | STATED | [Getting Started with the Control One (2021) @01:07](https://www.youtube.com/watch?v=eHgkltVdG-I&t=67), [@04:59](https://www.youtube.com/watch?v=eHgkltVdG-I&t=299), [@05:31](https://www.youtube.com/watch?v=eHgkltVdG-I&t=331) |
| 4.17 | **MIDI Clock** carries only a count, not a full time signal. Use Cue to start the show and Beat Shift to nudge the Autoloop a beat forward or back. | STATED | [MIDI Clock (2021) @02:50](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=170) |
| 4.18 | MIDI Clock and MTC sync in drive Autoloops. | STATED | [SoundSwitch 2.1 (2019) @02:15](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=135) |

### Q5. Recommended workflow (as SoundSwitch shows it)

| # | Fact | Type | Source |
|---|---|---|---|
| 5.1 | Accurate beatgrids in the DJ software are the key thing for Autoloops, since SoundSwitch's grid syncs to them. | STATED | [Autoloops Explained (2021) @08:31](https://www.youtube.com/watch?v=dwe6g-qczjI&t=511) |
| 5.2 | Set up the venue first. Group lights by location, name them, set the DMX addresses and confirm with a blue color override. Then set the fixture categories. | STATED | [AutoScripting Explained (2021) @01:40](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=100), [@04:23](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=263), [@04:56](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=296) |
| 5.3 | Fill in the Position and Attribute Cues before judging an Autoscript. Without them the movers won't do anything. | STATED | [AutoScripting Explained (2021) @08:20](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=500), [@09:29](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=569) |
| 5.4 | Set positions starting from the DJ booth and always move the lights outward, so they never point behind the booth. The positions are then roamed in an Autoloop: booth, forward, then the same order reversed. | STATED | [Working with Moving Head Lights (2018) @00:04](https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=4), [@00:36](https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=36) |
| 5.5 | Mounting orientation decides which corner of the pan/tilt pad to use. Pull the lights away from the wall behind you. | STATED | [Movement & Attribute Cues (2021) @04:44](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=284), [@05:20](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=320) |
| 5.6 | Autoscript the Autoloops, then keep re-applying presets with the dialog open (see 2.3). | STATED | [Autoloop AutoScripting (2023) @02:07](https://www.youtube.com/watch?v=5alSfsuWigQ&t=127) |
| 5.7 | **Drop loop recipe:** full strobe for the first 3 bars, a pulse on every bar, and a second strobe at bar 9 (the next phrase). DJ-booth positions go at the start and end, a few other position cues sit between, and Change & Hold (1 bar) closes it. | STATED | [Scripting Session: Autoloops and MIDI (2018) @00:35](https://www.youtube.com/watch?v=WpIH8pw1z84&t=35), [@01:06](https://www.youtube.com/watch?v=WpIH8pw1z84&t=66), [@01:44](https://www.youtube.com/watch?v=WpIH8pw1z84&t=104) |
| 5.8 | **Breakdown loop recipe:** fade out over the first 3 bars, hold the intensity flat, use slow simple color changes, and ramp the intensity up at the end toward the drop. A few position cues keep the movers going. | STATED | [Scripting Session: Autoloops and MIDI (2018) @01:44](https://www.youtube.com/watch?v=WpIH8pw1z84&t=104), [@02:18](https://www.youtube.com/watch?v=WpIH8pw1z84&t=138) |
| 5.9 | Copy selected tracks only between loops (Cmd-click the intensity and position tracks), for example everything except color. | STATED | [Scripting Session: Autoloops and MIDI (2018) @03:27](https://www.youtube.com/watch?v=WpIH8pw1z84&t=207) |
| 5.10 | Copying Main Track content to another Autoloop brings its Attribute Cues, Position Cues, color and intensity along. | STATED | [Advanced Features (2021) @05:36](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=336), [@06:06](https://www.youtube.com/watch?v=3_YZMGEKhjw&t=366) |
| 5.11 | Build a new loop: color transition first, then intensity (smooth pulse every bar, flat stretches, half-bar flash pulses), then mover colors, a movement effect, gobo Attribute Cues and Position Cues. | STATED | [Autoloops Explained (2021) @04:09](https://www.youtube.com/watch?v=dwe6g-qczjI&t=249), [@05:16](https://www.youtube.com/watch?v=dwe6g-qczjI&t=316), [@06:20](https://www.youtube.com/watch?v=dwe6g-qczjI&t=380) |
| 5.12 | The presenter's own practice: Autoscript the key tracks and let Autoloops cover the rest. | STATED | [Getting Started (2021) @10:13](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=613) |

---

## Contradictions and version drift

1. **Bank size.**
   - 2019: 4 banks of 8 = 32 ([fUVeC0Hs5fw @01:12](https://www.youtube.com/watch?v=fUVeC0Hs5fw&t=72)).
   - 2.9 (2024): 4 banks of 32 = 128 ([hj9oJqZJ55c @04:03](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=243)).
   - Version drift. 2.11 is 4x32.
2. **The bank autoplay control** is described three ways for one function, which is UI drift:
   - a toggle at the top right (2018);
   - a small switch at the top (2019);
   - a checkbox (2021).
3. **Did stock loops have fixture-track content?**
   - 2023 says they had Main Track effects only.
   - 2021 says the GigBar Move loops do have fixture-track effects.
   - Reconciled by 1.5: fixture-track content ships only for the GigBar Move venue. Any custom venue gets Main Track only.
4. **Starting a standalone show.**
   - 2019: the "LINK" button on the Standalone screen starts it with no DJ input.
   - 2021 Control One: Shift + Link starts Autoloops at 120 BPM.
   - 2.9: a Source selection menu with BPM Detection as one choice.
   - The early "LINK" may be the old label for the internal clock, or a caption error; Ableton Link proper (2018 videos) follows another app. Treat it as UI drift and check in 2.11. Unresolved.
5. **Repeat.**
   - 2021 says Repeat holds the current loop "until the end of the audio file".
   - The KB describes Repeat as Infinite or Track Duration.
   - Not contradictory, but the video describes only the track-length case.
6. **Overriding scripted tracks.**
   - 2019-2021: a global setting (Autoloop Override).
   - 2.9: any Autoloop can also be fired by hand over a scripted track.
   - Both exist (evolution, not conflict).
7. **Strobe override wording** (2019, 2.38) is ambiguous: the caption can be read as group strobe 0 silencing the group while some fixture track still strobes.

## Not covered by any video (gaps to check in the app or the KB)

- Exclusive bank (long-press).
- What BPM Detection does with neither silence box ticked, or what an Autoloop does when Link stops.
- How Autoscript treats Spot, Multi-cell or Strobe/Blinder categories, and how the Primary / Secondary / Tertiary colors map to fixtures.
- Which sections apply to Autoloops in the Autoscript dialog, and whether Autoloops have a phrase grid.
- Color-wheel fixtures (holding a wheel color versus RGB color changes).
- **Smoke inside Autoloops** (relevant to open item 2):
  - The videos say only that Attribute Cues switch a smoke machine on and off ([uSRTHbTTSaQ @07:28](https://www.youtube.com/watch?v=uSRTHbTTSaQ&t=448)).
  - They also say Autoscript places whichever Attribute Cues are in its "used" list ([0b22G5i4Ut4 @12:14](https://www.youtube.com/watch?v=0b22G5i4Ut4&t=734)).
  - INFERRED: an autoscripted loop with a smoke cue in its used list can fire the hazer. Set that cue's hazer value to 0, or remove it from the list.

## Video index

| Video | Date | URL |
|---|---|---|
| Scripting Session: Autoloops and MIDI | 2018-01-16 | https://www.youtube.com/watch?v=WpIH8pw1z84 |
| Quick Tips: Autoloop Overrides | 2019-01-15 | https://www.youtube.com/watch?v=LF548RAwFag |
| Quick Tips: Loop Auto-Strobe | 2019-01-15 | https://www.youtube.com/watch?v=xTonfl6g3AM |
| SoundSwitch Autoloops Explained | 2019-09-05 | https://www.youtube.com/watch?v=fUVeC0Hs5fw |
| SoundSwitch 2.1 | 2019-09-05 | https://www.youtube.com/watch?v=8JF6C-kpLxo |
| SoundSwitch 2.2 | 2020-03-26 | https://www.youtube.com/watch?v=Wis8O1gTWP8 |
| Autoloops Explained | 2021-08-24 | https://www.youtube.com/watch?v=dwe6g-qczjI |
| AutoScripting Explained | 2021-08-24 | https://www.youtube.com/watch?v=0b22G5i4Ut4 |
| Movement & Attribute Cues | 2021-08-24 | https://www.youtube.com/watch?v=uSRTHbTTSaQ |
| What's New in SoundSwitch 2.3 | 2021-08-24 | https://www.youtube.com/watch?v=HSue8aJVn8c |
| Autoloop AutoScripting | 2023-02-20 | https://www.youtube.com/watch?v=5alSfsuWigQ |
| Autoscript Phrase Editing | 2023-08-22 | https://www.youtube.com/watch?v=m_iJS6RE01Q |
| SoundSwitch 2.9 x BPM Detection | 2024-08-27 | https://www.youtube.com/watch?v=hj9oJqZJ55c |
| *Also cited:* Effects Generator Pt 1 (2016), Scripting Session 1 (2016), Advanced Chase Effects (2017), Working with Moving Head Lights (2018), Ableton LINK x Serato / Traktor / Live (2018), Custom Scripted Tracks Pt 1 and 4 (2018), Movement Shape FX (2019), Editing Colors, Strobe & Overrides (2019), Standalone Mode (2019), GigBar 2 Tutorial (2020), Advanced Features (2021), Getting Started (2021), Static Looks Explained (2021), MIDI Clock (2021), SoundSwitch X Virtual DJ (2021), Getting Started with the Control One (2021), Control One x Serato (2021) | | links inline above |
