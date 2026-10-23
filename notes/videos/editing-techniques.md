# SoundSwitch editing videos - extracted facts (set 3: editing, chases, strobe, overrides, movers)

Source: 23 official SoundSwitch YouTube videos, read from the auto-caption transcripts in
`/Users/tonyw/Dropbox/SoundSwitch/youtube-captions/txt/`. Read-only research, 2026-10-21.

**How to read this file**
- **[STATED]** = the presenter says it (paraphrased here). **[INFERRED]** = my reading of what was said or shown, not said outright.
- Every fact cites: short title, year, `[mm:ss]`, and a link with `&t=SECONDS`. Caption timestamps mark the **start of a caption block** (about 30 s long), so the moment can be up to ~30 s after the link point.
- **All videos are 2016-2019.** Tony runs SoundSwitch **2.11** (2026). Menus, names and dialogs may have moved. The videos say "Master Track"; 2.11 calls it the **Main Track** (per `notes/soundswitch-guide.md`).
- Captions are auto-generated, and some videos are almost silent (the narration is thin and much of the technique is only on screen). "Feature Mix - Effects Pt 1" is captions-only text overlays.
- Most videos script **songs**, not Autoloops. The editing timeline is the same kind of editor (one video adds position cues to an Autoloop directly), so most of it should carry over. **[INFERRED]**
- Where `notes/soundswitch-guide.md` or `notes/soundswitch-kb.md` (Tony's 2.11 notes) already confirm or contradict a fact, it is marked **Repo notes:**. That is not a video fact.

---

## Top 10 most useful techniques for dynamic loops

1. **Chases across selected fixture tracks (Effects Generator).** Select a time range across several fixture tracks, apply Forward / Reverse / Bounce / Follow chase, pick the timing. This is the tool for stepping the Tripars down the floor. (Effects Generator Pt 1 [01:20]; Custom Pt 1 [00:35]; Moving Head Lights [03:07])
2. **Two layers of chase: "inside the groups" vs "selected tracks".** Applied inside groups, each group chases its own members; applied to selected tracks, one chase runs across the tracks as units. Presenter does group-internal chases first, then an overall cross-group chase for the second half of a drop. (Custom Pt 4 [01:59]; Custom Pt 1 [02:18])
3. **Build-up escalation recipe:** same chase over everything, then the same chase faster in the next section, then a **Reverse** chase near the end of the build, then strobe + one color on the drop. (Custom Pt 4 [00:03]-[01:59])
4. **Position overrides per mover = movers stop moving as one.** A position override tells one light to stop following the Main Track; stagger different cues on each mover's override track to make a **position chase**. (Advanced Chase Effects [01:26]-[02:33])
5. **Change-and-hold cue pairs.** Drop a duplicate of the current position just before the next one, so the light holds, then moves, rather than drifting the whole time. (Advanced Chase Effects [01:59], [03:38]; Custom Pt 3 [00:45])
6. **Move the movers in the dark, and space moves far apart.** Change position during a blackout so the reposition isn't seen; spread position cues out for smooth, slow travel; cue at the start and end of each section. (Scripting Session 1 [07:09]-[07:39])
7. **Movement Shape FX on top of a position**, with size and speed set separately at the start and end of the selection (ramps) plus a direction setting. (Movement Shape FX [00:01]-[00:31])
8. **Intensity overrides for darkness and solo moments.** Keep movers off while other lights flash; black out the Main Track so one fixture (a laser in the video) plays alone. Fits Tony's "lone beam" idea. (Custom Pt 2 [01:46]; Custom Pt 3 [00:03])
9. **Strobe blocks with start/end rate ramps, aimed at build-ups and drop hits;** zero the strobe on a group override to keep chosen lights out of it. (Editing Colors, Strobe & Overrides [00:37]-[01:51]; Moving Head Lights [02:35]; Scripting Session 1 [05:35])
10. **Color transitions instead of fast palettes:** white-to-black for a fade to black before a drop (no intensity edit needed), a slow white-to-purple fade across a breakdown, and a contrasting color scheme on a subset of fixtures against the Main Track. (Editing Colors [00:37]; Scripting Session 1 [03:32], [04:47])

Honorable mention: **number-key pulse hot keys on a selection** (1 = 10% ... 0 = 100%, then pick timing) and **Link Blocks** (a linked copy of a master block) for fast, consistent repeats. (Editing with Hot Keys [01:07]; Advanced Editing Features [00:36])

---

## Source index

| ID | Title | Published | URL |
|---|---|---|---|
| vjgRslXhxvk | Editing Colors, Strobe & Overrides | 2019-06-11 | https://www.youtube.com/watch?v=vjgRslXhxvk |
| 0rGJjK5Vzb8 | Advanced Editing Features | 2019-06-12 | https://www.youtube.com/watch?v=0rGJjK5Vzb8 |
| 6naLETQrWCc | Controlling Intensity | 2019-06-12 | https://www.youtube.com/watch?v=6naLETQrWCc |
| CMtnwXKctAc | Adding Strobe Effects | 2019-06-12 | https://www.youtube.com/watch?v=CMtnwXKctAc |
| ETU2j9oqmGc | Color Picker | 2019-06-12 | https://www.youtube.com/watch?v=ETU2j9oqmGc |
| zozDwbhQcII | Color Transitions | 2019-06-12 | https://www.youtube.com/watch?v=zozDwbhQcII |
| sIEG0UPkIU0 | HEX Color Mixing in SoundSwitch | 2019-09-05 | https://www.youtube.com/watch?v=sIEG0UPkIU0 |
| oeSQze7-5n4 | Creating - Part One | 2019-06-12 | https://www.youtube.com/watch?v=oeSQze7-5n4 |
| a5Dqt0vSaP4 | Effects Generator Pt 1 | 2016-11-23 | https://www.youtube.com/watch?v=a5Dqt0vSaP4 |
| lYLdH1CFTmU | SoundSwitch Feature Mix - Effects Pt 1 | 2016-11-16 | https://www.youtube.com/watch?v=lYLdH1CFTmU |
| vAbUAUixupk | Editing with Hot Keys | 2016-11-23 | https://www.youtube.com/watch?v=vAbUAUixupk |
| EETBfocNxOY | Scripting Session 1 | 2016-11-30 | https://www.youtube.com/watch?v=EETBfocNxOY |
| pxU4nqV5ebw | Scripting Session: Advanced Chase Effects | 2017-10-08 | https://www.youtube.com/watch?v=pxU4nqV5ebw |
| pDpU-ZNfVCE | Scripting Session: Working with Moving Head Lights | 2018-02-22 | https://www.youtube.com/watch?v=pDpU-ZNfVCE |
| MWmxn4Ym2Ds | Scripting Session: Custom Scripted Tracks (Pt. 1) | 2018-09-12 | https://www.youtube.com/watch?v=MWmxn4Ym2Ds |
| fK5pkuX47CA | Scripting Session: Custom Scripted Tracks (Pt. 2) | 2018-09-13 | https://www.youtube.com/watch?v=fK5pkuX47CA |
| 8ooF-5rAkLY | Scripting Session: Custom Scripted Tracks (Pt. 3) | 2018-09-18 | https://www.youtube.com/watch?v=8ooF-5rAkLY |
| 1p7SDBxizKo | Scripting Session: Custom Scripted Tracks (Pt. 4) | 2018-09-17 | https://www.youtube.com/watch?v=1p7SDBxizKo |
| Gk1GfC1OQlM | Quick Tips: Movement Shape FX | 2019-01-15 | https://www.youtube.com/watch?v=Gk1GfC1OQlM |
| KuKEEwEYS44 | Quick Tips: Multiple Track Selection | 2019-01-15 | https://www.youtube.com/watch?v=KuKEEwEYS44 |
| L4QiDomsw94 | Quick Tips: Edit Mode Looping | 2019-01-15 | https://www.youtube.com/watch?v=L4QiDomsw94 |
| tNgaXXaRxqc | Quick Tips: Deleting Lighting Info | 2019-06-12 | https://www.youtube.com/watch?v=tNgaXXaRxqc |
| k3lCAwB0kU0 | Adding Beatgrids | 2019-06-11 | https://www.youtube.com/watch?v=k3lCAwB0kU0 |

Note: "Creating - Part One" (2019) is a compilation of the Color Picker, Controlling Intensity and Color Transitions clips, almost word for word. Facts from it are cited to the shorter clips where they repeat.

---

## 1. Hot keys

- **[STATED]** During playback, with the play marker inside the Main Track's beatgrid, the **number keys let you tap in intensity pulses** live, like drumming. Each number is 10%: 1 = 10%, 5 = 50%, **0 = 100%**.
  Editing with Hot Keys (2016) [00:06] https://www.youtube.com/watch?v=vAbUAUixupk&t=6 and [00:36] https://www.youtube.com/watch?v=vAbUAUixupk&t=36
- **[STATED]** **Selection pulse hot key:** make a selection, press a number key, and a dialog asks for the pulse timing (shown: every 1/8 bar). The selection fills with pulses at that level.
  Editing with Hot Keys (2016) [01:07] https://www.youtube.com/watch?v=vAbUAUixupk&t=67
- **[STATED]** **Single pulse without playback:** double-click to put the play marker where you want it, then press a number key.
  Editing with Hot Keys (2016) [01:07] https://www.youtube.com/watch?v=vAbUAUixupk&t=67 (and [01:37] https://www.youtube.com/watch?v=vAbUAUixupk&t=97)
- **[STATED]** **Shift + Q** quantizes the selection exactly to the beatgrid.
  Editing with Hot Keys (2016) [00:36] https://www.youtube.com/watch?v=vAbUAUixupk&t=36
- **[STATED]** **Shift + click-drag** on a selection moves the whole selection left or right (used to nudge pulses onto the grid).
  Editing with Hot Keys (2016) [00:36] https://www.youtube.com/watch?v=vAbUAUixupk&t=36; Advanced Editing Features (2019) [00:36] https://www.youtube.com/watch?v=0rGJjK5Vzb8&t=36
- **[STATED]** **Cmd+C / Cmd+V** (Ctrl on PC) copy and paste a selected section.
  Controlling Intensity (2019) [01:13] https://www.youtube.com/watch?v=6naLETQrWCc&t=73
- **[STATED]** **Cmd+Delete** (Ctrl+Delete) clears the data inside a selection; **Shift+Cmd+Delete** also clears override sections and Main Track attribute cues. Details in section 9.
  Quick Tips: Deleting Lighting Info (2019) [00:03] https://www.youtube.com/watch?v=tNgaXXaRxqc&t=3
- **[STATED]** **Spacebar** plays the track; inside the Color Transition dialog it switches from the start color to the end color.
  Adding Beatgrids (2019) [00:06] https://www.youtube.com/watch?v=k3lCAwB0kU0&t=6; Color Transitions (2019) [00:06] https://www.youtube.com/watch?v=zozDwbhQcII&t=6
- **[STATED]** In the Scripting Session the presenter uses a pulse hot key to put a **70% pulse** across a whole verse.
  Scripting Session 1 (2016) [01:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=95
- Repo notes (2.11, from the KB): Shift+P position override, Shift+O intensity override, Shift+S strobe, Shift+T color transition, keys 1-0 intensity pulses. The videos don't mention Shift+P/O/S/T.

## 2. Selecting, moving, quantizing, copying, Link Blocks

- **[STATED]** **Beatgrid snapping** toggles with the snapping icon. With it on, nodes snap as you move them; with it off, they move freely.
  Advanced Editing Features (2019) [00:06] https://www.youtube.com/watch?v=0rGJjK5Vzb8&t=6; Controlling Intensity (2019) [00:06] https://www.youtube.com/watch?v=6naLETQrWCc&t=6
- **[STATED]** **Quantize button:** select off-grid nodes, press Quantize, and they snap to the nearest grid line.
  Advanced Editing Features (2019) [00:06] https://www.youtube.com/watch?v=0rGJjK5Vzb8&t=6; Controlling Intensity (2019) [00:36] https://www.youtube.com/watch?v=6naLETQrWCc&t=36
- **[STATED]** **Link Blocks:** select some lighting data, right-click > **Create Master Block**; go further down the timeline, right-click > **Create Link Block**. A Link Block is a live duplicate: you can move or stretch it, and edits to the Master Block show up in every Link Block. Delete one with right-click > delete. The presenter calls it "a fancy Copy and Paste".
  Advanced Editing Features (2019) [00:36] https://www.youtube.com/watch?v=0rGJjK5Vzb8&t=36 and [01:10] https://www.youtube.com/watch?v=0rGJjK5Vzb8&t=70
- **[INFERRED]** Link Blocks suit Autoloops that repeat a 4- or 8-bar figure: change the master once and every repeat follows. Not tested in 2.11.
- **[STATED]** **Stretch a block** (color, color transition, strobe) by dragging its end. The presenter stretches a color from one section into the next to join the two sections.
  Editing Colors, Strobe & Overrides (2019) [01:11] https://www.youtube.com/watch?v=vjgRslXhxvk&t=71; Scripting Session 1 (2016) [01:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=95
- **[STATED]** After building a phrase, the presenter selects all the parts and copy-pastes them over the next eight bars.
  Custom Scripted Tracks Pt 2 (2018) [01:46] https://www.youtube.com/watch?v=fK5pkuX47CA&t=106

## 3. Intensity

- **[STATED]** **Click on the intensity graph to create a node;** build shapes from nodes and line them up with the kick drum in the waveform. The presenter prefers pulses joined into one connected shape rather than isolated spikes, but says to do what feels right.
  Controlling Intensity (2019) [00:06] https://www.youtube.com/watch?v=6naLETQrWCc&t=6
- **[STATED]** **Delete a node by double-clicking it,** or select a range and press Cmd+Delete to clear all nodes in it.
  Controlling Intensity (2019) [00:36] https://www.youtube.com/watch?v=6naLETQrWCc&t=36
- **[STATED]** **Effects menu intensity effects:** select a range on the Main Track (its length = the effect's length), then drag an effect from the effects menu onto it. Shown: **Fade In**, **Fade Out**, **Random Intensity** (a flicker effect).
  Effects Generator Pt 1 (2016) [00:04] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=4 and [00:41] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=41
- **[STATED]** **Effects stack by type:** with a color palette already applied to a range, the presenter keeps the range selected and drops a Fade Out on top, so color comes from the palette and the fade shapes intensity.
  Effects Generator Pt 1 (2016) [02:26] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=146
- **[STATED]** Some effects prompt for **timing** (shown: every 1/8 bar).
  Effects Generator Pt 1 (2016) [01:51] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=111
- **[STATED]** A **Fade In across a whole intro** raises the light level over the section; the presenter then brings the level down a bit before the verse.
  Scripting Session 1 (2016) [01:05] https://www.youtube.com/watch?v=EETBfocNxOY&t=65
- **[STATED]** For a breakdown he uses a fade-in effect over its full length, then a strobe on its second half as the build starts.
  Working with Moving Head Lights (2018) [02:35] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=155
- **[STATED]** In a custom section he picks out **specific sounds** in the track and puts pulses only on those, with an **alternating flash** between lights (pulse one track, copy it to another track).
  Custom Scripted Tracks Pt 2 (2018) [00:36] https://www.youtube.com/watch?v=fK5pkuX47CA&t=36 and [01:14] https://www.youtube.com/watch?v=fK5pkuX47CA&t=74
- **[INFERRED]** The alternating flash means the second light's pulses fall where the first light's don't (an A/B call and answer). The video shows it but doesn't explain the offset.
- Repo notes (2.11): applying an intensity effect by **double-clicking** it works; dragging was unreliable. The dialog asks for depth (min 10%) and beat length (1/32 to 1 bar). The videos only show drag and drop (see Contradictions).

## 4. Effects Generator: chases

- **[STATED]** SoundSwitch has several chase effects. Applying one by dragging it onto a **Group Track** and choosing **group** puts the effect on every fixture in that group.
  Effects Generator Pt 1 (2016) [00:41] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=41 and [01:20] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=80
- **[STATED]** **Across many fixtures:** select across all the fixture tracks, then drop a **Bounce chase**. Because the selection includes both groups and individual fixtures, SoundSwitch asks whether to apply it **within the groups** or **just to the selected fixtures**. The presenter picks selected fixtures.
  Effects Generator Pt 1 (2016) [01:20] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=80 and [01:51] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=111
- **[STATED]** "Selected tracks" means the effect is **not** placed inside the groups; "inside the groups" means the chase runs within each group.
  Custom Scripted Tracks Pt 1 (2018) [02:18] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=138; Custom Scripted Tracks Pt 4 (2018) [01:59] https://www.youtube.com/watch?v=1p7SDBxizKo&t=119
- **[INFERRED]** So with Tony's rig, "selected tracks" on the six Tripar tracks gives a front-to-back step; "within groups" on paired groups would chase inside each pair at the same time.
- **[STATED]** **Forward chase** on a multi-cell fixture (Core 3x3) shows, when the group is expanded, many pulses moving forward across the fixture's cells.
  Scripting Session 1 (2016) [02:54] https://www.youtube.com/watch?v=EETBfocNxOY&t=174
- **[STATED]** **Follow chase** options: untick **wrap** and raise the **light count** (to 15 in the video), then pick timing. SoundSwitch writes pulses onto every fixture track in the group.
  Custom Scripted Tracks Pt 1 (2018) [00:35] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=35 and [01:08] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=68
- **[INFERRED]** "Wrap" likely decides whether the chase loops back to the first light after the last one; "light count" likely sets how many cells/fixtures the chase spans. Neither is explained in the video.
- **[STATED]** **Bounce chase at 1/16 bar** for a section where the music speeds up.
  Custom Scripted Tracks Pt 1 (2018) [01:45] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=105
- **[STATED]** **Reverse chase** runs the lights in the opposite direction; used near the end of a build-up after forward chases.
  Custom Scripted Tracks Pt 4 (2018) [00:39] https://www.youtube.com/watch?v=1p7SDBxizKo&t=39
- **[STATED]** **Excluding lights from a chase:** collapse the fixture tracks of lights you don't want, select the ones you do, then apply a **Forward chase at 1/4** timing.
  Working with Moving Head Lights (2018) [03:07] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=187
- **[STATED]** **Color chase** (under Color in the Effects menu): select the range across all fixtures to include, drag Color Chase on, choose the **chase color** and **timing**.
  Advanced Chase Effects (2017) [03:06] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=186
- **[STATED]** **Pulse chase:** select the range, drop the **Forward chase**, choose timing; the presenter says this gives a pulse chase every quarter beat.
  Advanced Chase Effects (2017) [03:38] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=218 and [04:08] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=248
- **[STATED]** Chase types named across these videos: Forward, Reverse, Bounce, Follow, Color Chase, plus a position chase built by hand (section 8). The Feature Mix overlays advertise intensity, color and chase effects, combining chase with color, effects on individual fixtures, and mixing fixture and group effects.
  Feature Mix - Effects Pt 1 (2016) [00:11] https://www.youtube.com/watch?v=lYLdH1CFTmU&t=11
- **Not in these videos:** a "random" chase order, or a per-fixture offset/phase setting for chases. Only **random intensity** (flicker) and **random color** are shown. **[STATED by absence]**

## 5. Color

- **[STATED]** **Apply a color:** select a range on the Main Track, right-click > **Change Color**. Pick in the picker or type an exact RGB value. A color block appears in the Color Track.
  Color Picker (2019) [00:05] https://www.youtube.com/watch?v=ETU2j9oqmGc&t=5 and [00:35] https://www.youtube.com/watch?v=ETU2j9oqmGc&t=35
- **[STATED]** **Swatches:** the picker shows recent colors; save one as a swatch with the **+** in the swatches menu; delete a swatch by selecting it and pressing Delete.
  Color Picker (2019) [00:05] https://www.youtube.com/watch?v=ETU2j9oqmGc&t=5 and [00:35] https://www.youtube.com/watch?v=ETU2j9oqmGc&t=35
- **[INFERRED]** Swatches are the natural place to keep each stack's palette, so every loop in a stack uses the same exact RGB values.
- **[STATED]** **Amber, White and UV mixing** (added by Sept 2019): choose the RGB value, then add Amber, White or UV. Adding UV shows a **crosshatch** pattern on the Color Track. Example: red RGB base plus White and UV.
  HEX Color Mixing (2019) [00:04] https://www.youtube.com/watch?v=sIEG0UPkIU0&t=4 and [00:36] https://www.youtube.com/watch?v=sIEG0UPkIU0&t=36
- **[STATED]** **Color Transition:** select the range, right-click > Color Transition tool, pick the start color, press **spacebar** (or click the end marker), pick the end color. Example: red to blue; white back to blue placed just after a snare.
  Editing Colors, Strobe & Overrides (2019) [00:06] https://www.youtube.com/watch?v=vjgRslXhxvk&t=6; Color Transitions (2019) [00:06] https://www.youtube.com/watch?v=zozDwbhQcII&t=6 and [00:37] https://www.youtube.com/watch?v=zozDwbhQcII&t=37
- **[STATED]** **Fade to black without touching intensity:** a Color Transition from **white to black**. Used just before a drop.
  Editing Colors, Strobe & Overrides (2019) [00:37] https://www.youtube.com/watch?v=vjgRslXhxvk&t=37
- **[STATED]** **Color palettes** (22 new in 2016): select a range, drag a palette on, choose how often the colors change. In the Scripting Session the intro palette changes **every 1 bar**, on the Main Track, so the whole rig plays it.
  Effects Generator Pt 1 (2016) [02:26] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=146; Feature Mix (2016) [00:43] https://www.youtube.com/watch?v=lYLdH1CFTmU&t=43; Scripting Session 1 (2016) [00:34] https://www.youtube.com/watch?v=EETBfocNxOY&t=34
- **[STATED]** **Random color effect** on the Main Track, with a timing prompt.
  Effects Generator Pt 1 (2016) [01:51] https://www.youtube.com/watch?v=a5Dqt0vSaP4&t=111
- **[INFERRED]** For Tony's "slow color changes" rule, palette and random color effects are a poor fit at 1-bar timing (that's a change every ~2 s at 124 BPM). Hand-placed Color Transitions over many bars match his rule better. Whether palettes accept timings longer than 1 bar isn't shown.
- **[STATED]** **Contrasting scheme on a subset:** warm palette (yellows, oranges, reds) on the Main Track, then a **blue** scheme on some of the other fixtures.
  Scripting Session 1 (2016) [03:32] https://www.youtube.com/watch?v=EETBfocNxOY&t=212 and [04:02] https://www.youtube.com/watch?v=EETBfocNxOY&t=242
- **[STATED]** **Breakdown:** light fades out while the color changes **white to purple**; the same color holds for the second half.
  Scripting Session 1 (2016) [04:47] https://www.youtube.com/watch?v=EETBfocNxOY&t=287
- **[STATED]** On the second drop the presenter wants every light red and strobing.
  Custom Scripted Tracks Pt 4 (2018) [01:28] https://www.youtube.com/watch?v=1p7SDBxizKo&t=88

## 6. Strobe

- **[STATED]** A **Strobe Effect** works like a Color Transition, but you set the **strobe intensity at the start and at the end** of the selection with sliders. Applying it puts a **Strobe Block** on the Strobe Track. Stretch the block's end to change its length.
  Adding Strobe Effects (2019) [00:07] https://www.youtube.com/watch?v=CMtnwXKctAc&t=7; Editing Colors, Strobe & Overrides (2019) [00:37] https://www.youtube.com/watch?v=vjgRslXhxvk&t=37 and [01:11] https://www.youtube.com/watch?v=vjgRslXhxvk&t=71
- **[STATED]** The 2018 video calls the same start/end control the **strobe rate**.
  Working with Moving Head Lights (2018) [02:35] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=155
- **[INFERRED]** A start-low, end-high strobe block is a rate ramp, the classic build-up riser.
- **[STATED]** **Strobe can be overridden on Group and Fixture tracks.** Set a group's strobe to **0** and its lights won't strobe.
  Editing Colors, Strobe & Overrides (2019) [01:51] https://www.youtube.com/watch?v=vjgRslXhxvk&t=111; Adding Strobe Effects (2019) [00:40] https://www.youtube.com/watch?v=CMtnwXKctAc&t=40
- **[STATED]** He then adds that the fixture track still strobes in time with the Main Track. (Ambiguous, see Contradictions.)
  Adding Strobe Effects (2019) [01:13] https://www.youtube.com/watch?v=CMtnwXKctAc&t=73
- **[STATED]** Strobe placement in the shows: first **two bars of a drop**; second half of a breakdown as it builds; on the movers only while chases run on the LED sticks; in time with a **stutter** effect in the music.
  Scripting Session 1 (2016) [05:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=335; Working with Moving Head Lights (2018) [02:35] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=155; Custom Pt 4 (2018) [01:28] https://www.youtube.com/watch?v=1p7SDBxizKo&t=88; Custom Pt 2 (2018) [02:52] https://www.youtube.com/watch?v=fK5pkuX47CA&t=172
- **Not in these videos:** what a dedicated strobe fixture (like the Shocker) needs to fire. **[INFERRED]** It needs a Strobe Block on a track it follows and intensity above 0 there; matches the repo's existing inference in `notes/soundswitch-kb.md`.

## 7. Overrides and track precedence

- **[STATED]** **Position overrides tell a particular light to stop following the Master Track.** Make one: select a range in a mover's position track, right-click > **Create Position Override**. Repeat for each mover in the effect.
  Advanced Chase Effects (2017) [01:26] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=86
- **[STATED]** Inside an override, the mover holds the Main Track's position until it reaches the override's own cue, then follows the override.
  Advanced Chase Effects (2017) [02:33] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=153
- **[STATED]** Color, intensity and strobe can all be overridden on Group and Fixture tracks; the strobe override is presented as working the same way as the color and intensity ones.
  Editing Colors, Strobe & Overrides (2019) [01:51] https://www.youtube.com/watch?v=vjgRslXhxvk&t=111
- **[STATED]** The Deleting video shows **intensity, color and position overrides** on tracks at once.
  Quick Tips: Deleting Lighting Info (2019) [00:03] https://www.youtube.com/watch?v=tNgaXXaRxqc&t=3
- **[STATED]** **Stretch intensity overrides** so the movers stay **off** while other lights flash.
  Custom Scripted Tracks Pt 2 (2018) [01:46] https://www.youtube.com/watch?v=fK5pkuX47CA&t=106
- **[STATED]** **Solo one fixture:** copy the Main Track's automation onto the laser's Fixture Track, then **black out the Main Track** so only the laser is on.
  Custom Scripted Tracks Pt 3 (2018) [00:03] https://www.youtube.com/watch?v=8ooF-5rAkLY&t=3
- **[INFERRED]** Precedence shown across the videos: **Fixture track > Group track > Main Track.** A track's own data replaces what it would inherit (the laser keeps playing while the Main Track is black; fixtures given their own blue scheme stay blue under a warm Main Track). Repo notes (2.11, KB) say the same: "Fixture and Group tracks override the Master Track", and "a member track with its own data overrides the group."
- **[STATED]** **Main Track data is portable:** everything on it, positions included, plays back on any venue/rig, and position cues re-map once the new venue's movers are aimed. (Fixture-track work is rig-specific, by implication.)
  Scripting Session 1 (2016) [08:12] https://www.youtube.com/watch?v=EETBfocNxOY&t=492 and [08:43] https://www.youtube.com/watch?v=EETBfocNxOY&t=523
- **[INFERRED]** For Autoloops the same holds: the more lives on the Main Track, the more a loop survives fixture swaps; per-fixture overrides are what make it look designed.
- Removing overrides: see section 9.

## 8. Moving heads: positions, movement shapes, and not moving as one

- **[STATED]** **Edit positions:** double-click a position to open the positions menu (X/Y pad), pick the position, select the movers, drag their dots, Apply.
  Advanced Chase Effects (2017) [00:55] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=55; Scripting Session 1 (2016) [06:38] https://www.youtube.com/watch?v=EETBfocNxOY&t=398
- **[STATED]** The presenter's two movers are on opposite sides, with **pan and tilt inverted on one** of them.
  Scripting Session 1 (2016) [06:38] https://www.youtube.com/watch?v=EETBfocNxOY&t=398
- **[INFERRED]** An inverted mover mirrors the other on the same cue, so a pair moves symmetrically instead of in parallel. Set in the venue patch, not on the timeline.
- **[STATED]** **Cue placement:** start at home, arrive at a position crossing over the DJ booth by the end of the intro; put the **same position cue at the end of the verse** so they hold; switch to the next position **during the blackout** before the chorus; cues at the start and end of each section.
  Scripting Session 1 (2016) [07:09] https://www.youtube.com/watch?v=EETBfocNxOY&t=429 and [07:39] https://www.youtube.com/watch?v=EETBfocNxOY&t=459
- **[STATED]** "I like to space my movements quite far apart" (paraphrase: it gives smooth, easy transitions between positions).
  Scripting Session 1 (2016) [07:39] https://www.youtube.com/watch?v=EETBfocNxOY&t=459
- **[STATED]** **Position chase recipe:** (1) set the positions; (2) create a position override on each mover; (3) place cues on the override tracks, spaced to different sounds, with a cue placed **in front of** each target (in reverse order) so the light changes and then holds before moving on.
  Advanced Chase Effects (2017) [00:55]-[02:33] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=55 , https://www.youtube.com/watch?v=pxU4nqV5ebw&t=119
- **[STATED]** **Change-and-hold:** adding cues as back-to-back pairs makes the fixture change, hold, then move to the next position. Also a duplicate cue further down to make a position hold.
  Custom Scripted Tracks Pt 3 (2018) [00:45] https://www.youtube.com/watch?v=8ooF-5rAkLY&t=45; Advanced Chase Effects (2017) [03:38] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=218
- **[INFERRED]** Without a hold cue, the mover glides continuously from one cue to the next across the whole gap. So cue spacing sets move speed: wide gaps = slow travel, a pair close together = a snap.
- **[STATED]** Position cues placed on specific sounds in the music make a laser (or mover) hit the beats.
  Custom Scripted Tracks Pt 3 (2018) [00:03] https://www.youtube.com/watch?v=8ooF-5rAkLY&t=3
- **[STATED]** **Mobile-DJ safety:** never point lights behind the DJ booth. Set the DJ booth position first, then build each next position by moving **outward** from it.
  Working with Moving Head Lights (2018) [00:04] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=4 and [00:36] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=36
- **[STATED]** **Roam-and-return in an Autoloop:** add the positions in order outward from the booth, then the same positions in **reverse order**, so the movers roam out and come back.
  Working with Moving Head Lights (2018) [00:36] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=36 and [01:19] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=79
- **[STATED]** **Movement Shape FX:** select a range, right-click > create a **Movement Effect**, choose the **shape**, set **size and speed at the start and at the end** of the selection, and set the **direction**. The shape runs **on top of the current position** (a circle around the selected position in the demo).
  Quick Tips: Movement Shape FX (2019) [00:01] https://www.youtube.com/watch?v=Gk1GfC1OQlM&t=1 and [00:31] https://www.youtube.com/watch?v=Gk1GfC1OQlM&t=31
- **[STATED]** **Fixture-built-in movement macros via attribute cues:** set an attribute cue that turns on the Intimidator Trio's built-in movement macros, adjust their speed; place a second attribute cue at the end of the section to turn them off.
  Custom Scripted Tracks Pt 4 (2018) [00:39] https://www.youtube.com/watch?v=1p7SDBxizKo&t=39 and [01:28] https://www.youtube.com/watch?v=1p7SDBxizKo&t=88
- **[STATED]** Autoscript has a **moving-head speed** (placement speed) setting, plus overall intensity, bridge intensity, pulse intensity and color-change speed.
  Working with Moving Head Lights (2018) [01:51] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=111; Custom Scripted Tracks Pt 1 (2018) [00:03] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=3

**How to keep movers from moving as one (summary)**

| Method | Evidence |
|---|---|
| Position override on each mover, with cues staggered in time (position chase) | **[STATED]** Advanced Chase Effects [01:26] |
| Different target positions per mover on their override tracks | **[INFERRED]** from the same recipe; Tony's 841 Logo override already does this for one fixture |
| Inverted pan/tilt on one of a pair (mirror) | **[STATED]** that it's set; **[INFERRED]** that it mirrors |
| Movement Shape FX with a different direction per mover | **[STATED]** a direction setting exists; **[INFERRED]** per-fixture use. Repo notes (2.11): a **Reverse** option flips direction "so a pair can circle against each other" |
| Different shape or size/speed ramp per mover track | **[INFERRED]**, not shown |
| Fixture's own movement macros via attribute cue | **[STATED]** Custom Pt 4 [00:39] (each fixture runs its own macro) |
| Per-fixture phase/offset setting inside a Movement Effect | **Not covered** in any of these videos |

## 9. Deleting and removing overrides

- **[STATED]** Two delete commands:
  - **Cmd/Ctrl + Delete** clears the **data inside** the selection (e.g. the color in a color override and the intensity inside an intensity override) but **keeps the override sections**. You then have to right-click to delete each override section.
  - **Shift + Cmd/Ctrl + Delete** clears the data **and** the override sections.
  Quick Tips: Deleting Lighting Info (2019) [00:03] https://www.youtube.com/watch?v=tNgaXXaRxqc&t=3 and [00:38] https://www.youtube.com/watch?v=tNgaXXaRxqc&t=38
- **[STATED]** On the Main Track, **Shift+Cmd+Delete** clears **attribute cues and intensity**; **Cmd+Delete** clears intensity but **keeps attribute cues**.
  Quick Tips: Deleting Lighting Info (2019) [01:21] https://www.youtube.com/watch?v=tNgaXXaRxqc&t=81
- **[STATED]** A Link Block is removed with right-click > delete.
  Advanced Editing Features (2019) [01:10] https://www.youtube.com/watch?v=0rGJjK5Vzb8&t=70
- **[STATED]** Workflow: run Automation (Autoscript), then **delete the parts you want to hand-build** (including the Main Track, to work on lights individually).
  Custom Scripted Tracks Pt 2 (2018) [00:03] https://www.youtube.com/watch?v=fK5pkuX47CA&t=3 and [00:36] https://www.youtube.com/watch?v=fK5pkuX47CA&t=36
- Repo notes (2.11) agree: Shift+Cmd+Delete clears data and overrides so the track inherits again; right-click on an override shows Delete Override.

## 10. Looping, library multi-select, beatgrids, phrase markers

- **[STATED]** **Edit Mode looping:** select a range in the **waveform**, right-click > loop the selection; right-click again to clear the loop. Meant to make building effects easier.
  Quick Tips: Edit Mode Looping (2019) [00:02] https://www.youtube.com/watch?v=L4QiDomsw94&t=2
- **[STATED]** **Library multi-select:** Cmd/Ctrl-click several tracks, right-click > **delete the lighting files** or **batch script** them.
  Quick Tips: Multiple Track Selection (2019) [00:02] https://www.youtube.com/watch?v=KuKEEwEYS44&t=2
- **[STATED]** **Adding a beatgrid:** play (spacebar) to find the first downbeat, double-click the waveform to put the play marker there, press **Add Beatgrid** in the toolbar, then drag the next downbeat marker onto the next downbeat; check alignment through the track with the navigation bar; **lock** the beatgrid with the lock icon. The icon to its left toggles beat snapping.
  Adding Beatgrids (2019) [00:06] https://www.youtube.com/watch?v=k3lCAwB0kU0&t=6 and [00:43] https://www.youtube.com/watch?v=k3lCAwB0kU0&t=43
- **[STATED]** The "Beatgrid ruler" lets you highlight and work one section at a time (intro, verse, chorus...).
  Scripting Session 1 (2016) [00:34] https://www.youtube.com/watch?v=EETBfocNxOY&t=34
- **[STATED]** In 2016 Autoloops were described as triggering and syncing on their own to the **Serato DJ** beatgrid. (Old context; 2.11 has more tempo sources.)
  Scripting Session 1 (2016) [00:02] https://www.youtube.com/watch?v=EETBfocNxOY&t=2
- **Phrase markers:** **not mentioned in any of these 23 videos.**

## 11. Presenter tips for good-looking shows (show structure)

- **[STATED]** Build in layers: Main Track first (color + intensity for everyone), then individual fixtures (chases, contrasting colors).
  Scripting Session 1 (2016) [02:20] https://www.youtube.com/watch?v=EETBfocNxOY&t=140
- **[STATED]** Leave the room **dark just before the drop**, then ramp up and hit the drop.
  Scripting Session 1 (2016) [02:20] https://www.youtube.com/watch?v=EETBfocNxOY&t=140 and [05:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=335
- **[STATED]** Play it back as you go and adjust levels and colors.
  Scripting Session 1 (2016) [01:05] https://www.youtube.com/watch?v=EETBfocNxOY&t=65
- **[STATED]** Tie sections together by stretching a color from one into the next.
  Scripting Session 1 (2016) [01:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=95
- **[STATED]** Small fade-out at the end of a track.
  Scripting Session 1 (2016) [06:06] https://www.youtube.com/watch?v=EETBfocNxOY&t=366
- **[STATED]** Match effect speed to the music: slower chase where it's sparse, 1/16 bounce where it speeds up; build-ups get faster, then reverse direction toward the end.
  Custom Pt 1 (2018) [01:45] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=105; Custom Pt 4 (2018) [00:03] https://www.youtube.com/watch?v=1p7SDBxizKo&t=3 and [00:39] https://www.youtube.com/watch?v=1p7SDBxizKo&t=39
- **[STATED]** Sometimes go simple: one effect over all fixtures together for a build.
  Custom Pt 4 (2018) [00:03] https://www.youtube.com/watch?v=1p7SDBxizKo&t=3
- **[STATED]** Start from Autoscript with tuned settings, then replace sections by hand.
  Custom Pt 1 (2018) [00:03] https://www.youtube.com/watch?v=MWmxn4Ym2Ds&t=3; Custom Pt 2 (2018) [00:03] https://www.youtube.com/watch?v=fK5pkuX47CA&t=3
- **[INFERRED]** Several tips line up with Tony's own rules: solo moments (laser alone), movers off while others flash, contrasting palette on a subset, slow position moves with holds. The presenters' 1-bar palette changes and random color effects do **not** fit his slow-color rule.

---

## Contradictions and ambiguities

1. **Strobe override, group vs fixture.** The video says a group strobe of 0 stops the lights in the group from strobing, then: "However, the fixture track will still strobe in time with the Master Track." Read literally these conflict. Likely meaning **[INFERRED]**: the fixture track shown either sits outside that group or carries its own strobe data, which beats the group (repo notes: "a member track with its own data overrides the group"). Test before relying on it.
   Adding Strobe Effects (2019) [00:40]/[01:13] https://www.youtube.com/watch?v=CMtnwXKctAc&t=40 , https://www.youtube.com/watch?v=CMtnwXKctAc&t=73
2. **Strobe "intensity" vs "rate".** 2019 videos call the start/end sliders strobe intensity; the 2018 video calls them strobe rate. Probably the same control. **[INFERRED]**
   Editing Colors (2019) [00:37] https://www.youtube.com/watch?v=vjgRslXhxvk&t=37 vs Moving Head Lights (2018) [02:35] https://www.youtube.com/watch?v=pDpU-ZNfVCE&t=155
3. **Timing units.** Narrators speak of quarter-beat timing (2016, 2017), 1/4 timing (2018) and eighth-of-a-bar timing (2016). Repo notes say the 2.11 dialog runs 1/32 to 1 **bar**, so the quarter-beat wording most likely means 1/4 bar = one beat. **[INFERRED]**
   Scripting Session 1 [01:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=95; Advanced Chase Effects [04:08] https://www.youtube.com/watch?v=pxU4nqV5ebw&t=248
4. **Scripting Session 1 narration slip:** he says "a pulse on every bar", then in the next breath a 70% pulse on every quarter beat. One of them is wrong; the screen would tell.
   Scripting Session 1 (2016) [01:35] https://www.youtube.com/watch?v=EETBfocNxOY&t=95
5. **Applying effects: drag vs double-click.** The 2016-2018 videos drag effects from the menu onto the selection. Tony's 2.11 notes found dragging intensity effects unreliable and double-clicking the effect reliable. Version/UI difference, not a factual conflict.
6. **Quantize: button (2019) vs Shift+Q (2016).** Two routes to the same thing, not a conflict; Shift+Q in 2.11 is unverified.
7. **Naming drift:** "Master Track" (videos) = "Main Track" (2.11). "Create a Movement Effect" (2019 video) vs "Apply Movement Effect" (repo notes, 2.11). "Strobe lock"/"color lock" in captions are mis-transcriptions of **block**.
8. **Publish order:** Custom Scripted Tracks Pt 4 (2018-09-17) was published a day before Pt 3 (2018-09-18). Content order is still 1-2-3-4.

## Not covered by these videos (gaps to research elsewhere)
- Per-fixture **offset/phase** for chases or movement shapes.
- A **random-order** chase.
- **Phrase markers**.
- What a dedicated strobe fixture needs to fire.
- Autoloop-specific behavior (loop length, bank switching). Only "Working with Moving Head Lights" edits an Autoloop directly.
- Color wheel fixtures (holding a wheel color); every color example here is RGB(+AWUV).
