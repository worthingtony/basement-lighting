# Facts 4 - Performance: Control One, Static Looks, tempo sources, idle, live operation

From the official SoundSwitch YouTube transcripts in `/Users/tonyw/Dropbox/SoundSwitch/youtube-captions/txt/` (auto-captions, read 2026-10-21). Everything is paraphrased.

**How to read this**
- **STATED** means the video says or shows it (as far as a caption can show it). **INFERRED** means it's my reading, from context or from several videos together.
- `[mm:ss]` is the start of the caption chunk that holds the fact, and the `&t=` link jumps there. The fact may be a few seconds further in.
- Captions garble names. "Autoloop back button" is almost certainly "bank button", and "the last show" is "the light show". I fixed these silently where the meaning is obvious and flagged them where it isn't.
- **The videos are 2016-2026. Tony runs 2.11.** Most of the Control One material is from 2021, which is SoundSwitch 2.5-era. Version drift is flagged in section 9.
- A few videos outside the assigned list were relevant, so I read them too. They're marked **(extra)**: Getting Started 2021, Autoloops Explained 2021, SoundSwitch 2.9 x BPM Detection 2024, What's New in 2.3, SoundSwitch 2.1, and the Quick Tips on Autoloop Overrides and Loop Auto-Strobe.

---

## Saturday checklist (the 8 most useful facts)

| # | Fact | Status | Source |
|---|---|---|---|
| 1 | **Link setup for a guest laptop:** put both computers on the same network. Turn Link on in the DJ software (in Serato it's a Link button at the top left), then turn Link on in SoundSwitch. SoundSwitch's BPM then follows the DJ's pitch fader. Autoloops, Static Looks and the MIDI overrides all still work while Link is synced. | STATED (2018 video, SoundSwitch 1.x era) | SoundSwitch x Ableton LINK x Serato DJ (2018) [00:09](https://www.youtube.com/watch?v=_udEdlyecGY&t=9), [00:42](https://www.youtube.com/watch?v=_udEdlyecGY&t=42) |
| 2 | **No video covers what Link does when the DJ hands over, stops, or pauses.** Link only demonstrates tempo following. Nothing shows start/stop, pause, upfader dimming or scripted tracks working over Link, so expect Autoloops only, with no pause and no fader dimming. If the guest plays **Virtual DJ**, a better route exists: SoundSwitch can connect to VDJ on *another computer* over OS2L by IP address, and that carries pause, playhead and faders. | Link gap: INFERRED (absence). VDJ over IP: STATED | SoundSwitch 2.1 (2019) (extra) [04:02](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=242); SoundSwitch X Virtual DJ (2021) [01:11](https://www.youtube.com/watch?v=pbON1Ce46OE&t=71) |
| 3 | **Fallback with no DJ software, on the Control One:** in Performance mode, hold **Shift + the Link (BPM TAP) button**. Autoloops start at **120 BPM**. Tap BPM to match the music. **Shift + Play/Pause** resets the phrase so the loop lands on the downbeat. Otherwise every control works exactly as it does with DJ software connected. | STATED | Getting Started with the Control One (2021) [04:59](https://www.youtube.com/watch?v=eHgkltVdG-I&t=299), [05:31](https://www.youtube.com/watch?v=eHgkltVdG-I&t=331), [06:02](https://www.youtube.com/watch?v=eHgkltVdG-I&t=362) |
| 4 | **BPM Detection settings:** a USB audio interface is the ideal input. Set the threshold line just above the room's ambient noise. Below the threshold, pick **Blackout** or **Pause Autoloops**. Use a lower refresh rate for open-format sets (80s/90s) and a higher one for steady house. Set a BPM range. Detection runs at every volume level, so the threshold only decides blackout or pause. | STATED | SoundSwitch 2.9 x BPM Detection (2024) (extra) [00:01](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=1), [01:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=92), [02:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=122), [02:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=152) |
| 5 | **Pause means freeze, not blackout.** When the DJ pauses, the light show pauses, and SoundSwitch's play/pause is described as a way to freeze the lights where they are. No video says that a stop goes dark. Blackout on silence is offered only by BPM Detection (#4). This matches the held, lit frame Tony saw on 10-20. | Pause and freeze: STATED. "Stays lit": INFERRED | Getting Started (2021) (extra) [04:46](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=286); Control One x Serato DJ (2021) [03:20](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=200) |
| 6 | **Keep genres apart with bank controls.** A bank button plays that bank alone. Shift + bank goes back to "play all banks", which plays *every* bank's Autoloops at random. Each bank also has an autoplay switch, so a bank of special looks (drops, strobes) only fires when you press it. Next, previous, repeat and sequential/random are also available. | STATED | Control One x Serato DJ (2021) [06:08](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=368); Autoloops Explained (2021) (extra) [09:36](https://www.youtube.com/watch?v=dwe6g-qczjI&t=576), [10:38](https://www.youtube.com/watch?v=dwe6g-qczjI&t=638), [11:09](https://www.youtube.com/watch?v=dwe6g-qczjI&t=669) |
| 7 | **Latch effects you want to leave on.** Every override button can be set to **press** (on only while held) or **toggle** (latches). Right-click it in the desktop app to choose. Toggle mode keeps an effect running "even if my hands aren't on the controller". The pad LEDs show what's latched. That includes a Static Look still running under Autoloop mode, and a Position override sitting under a color pad. | STATED | Control One x Serato DJ (2021) [04:59](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=299), [05:33](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=333), [06:39](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=399) |
| 8 | **Static Looks override only the fixtures you activate in them.** Fixtures left inactive keep following the Autoloop, even when you change Autoloops underneath. Static Looks aren't synced to the music, so they suit moments with no beat: the video names first dance, dinner and speeches; for Tony, the gap between DJs (INFERRED). | STATED | Static Looks Explained (2021) [00:33](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=33), [05:15](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=315), [05:46](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=346) |

---

## 1. Control One: every control the videos describe

The main source is **Getting Started with the Control One** (2021-11-23), `eHgkltVdG-I`. The panel has three sections: top (screen and main controls), upper middle (overrides), and lower (pads and intensity). STATED [01:07](https://www.youtube.com/watch?v=eHgkltVdG-I&t=67).

| Control | What it does | Status | Source |
|---|---|---|---|
| **USB switch** | Picks which USB input (port 1 or 2) is live. If it's on the wrong port, the screen warns you. | STATED | Control One Getting Started [01:07](https://www.youtube.com/watch?v=eHgkltVdG-I&t=67); Control One x Serato DJ [01:10](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=70) |
| **Play/Pause** | Plays or pauses the light show. | STATED | Control One Getting Started [01:07](https://www.youtube.com/watch?v=eHgkltVdG-I&t=67) |
| **Shift + Play/Pause** | Resets the Autoloop's phrase so it's back on the downbeat. The 2.9 video calls this resetting the phase to beat 1. | STATED | Control One Getting Started [05:31](https://www.youtube.com/watch?v=eHgkltVdG-I&t=331); 2.9 BPM Detection (extra) [03:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=182) |
| **SHIFT** | Switches buttons to their shift functions. | STATED | Control One Getting Started [01:07](https://www.youtube.com/watch?v=eHgkltVdG-I&t=67) |
| **BPM TAP** | Tap in the tempo. The same button also turns Link on and off. | STATED | Control One Getting Started [01:07](https://www.youtube.com/watch?v=eHgkltVdG-I&t=67), [01:38](https://www.youtube.com/watch?v=eHgkltVdG-I&t=98) |
| **Shift + Link (TAP)** | In Performance mode, starts Autoloops at 120 BPM with no DJ software. | STATED | Control One Getting Started [04:59](https://www.youtube.com/watch?v=eHgkltVdG-I&t=299) |
| **Autoloop Override** | Overrides scripted tracks, so only Autoloops play. | STATED | Control One Getting Started [01:38](https://www.youtube.com/watch?v=eHgkltVdG-I&t=98); Quick Tips: Autoloop Overrides (2019) (extra) [00:02](https://www.youtube.com/watch?v=LF548RAwFag&t=2) |
| **Two dials (center)** | Set the speed and the color/attribute of the effects launched below them. | STATED | Control One Getting Started [01:38](https://www.youtube.com/watch?v=eHgkltVdG-I&t=98) |
| **Menu / screen** | Sets the effect parameters for Movement, Strobe and Hue, sets which Position Cues the Position overrides use, has Settings (DMX output: **USB or Thru**), and Info (firmware). | STATED | Control One Getting Started [01:38](https://www.youtube.com/watch?v=eHgkltVdG-I&t=98) |
| **Menu > Effects > Movement** | Picks the Movement button's shape: figure eight, circle, horizontal scan or vertical scan. No desktop needed. | STATED | Control One x Serato DJ [04:24](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=264) |
| **Shift + an effect button** | Dial in that effect's parameters *before* launching it. | STATED | Control One Getting Started [02:14](https://www.youtube.com/watch?v=eHgkltVdG-I&t=134) |
| **Top row: MOVEMENT, STROBE, HUE, SMOKE** | Override effects layered on top of whatever is playing. The caption reads "movement, strobe, hue, color filter and smoke". "Hue" and "color filter" are probably one button (the "hue color filter"), so four buttons; see section 9. | STATED (list). Count of four: INFERRED | Control One Getting Started [02:14](https://www.youtube.com/watch?v=eHgkltVdG-I&t=134), [02:45](https://www.youtube.com/watch?v=eHgkltVdG-I&t=165) |
| **MOVEMENT** (behavior) | Moves the movers in the chosen shape. Size and speed are adjustable. | STATED | Getting Started (extra) [03:14](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=194), [03:44](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=224) |
| **HUE** (behavior) | A color filter. Turn it on, then turn the color dial, and the output shifts toward that hue. | STATED | Getting Started (extra) [04:15](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=255); What's New in 2.3 (extra) [01:39](https://www.youtube.com/watch?v=HSue8aJVn8c&t=99) |
| **STROBE** (behavior) | Strobes the lights. The speed dial sets the rate. | STATED | Getting Started (extra) [04:15](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=255) |
| **SMOKE** (behavior) | Described as the control for smoke machines. No video says how much output it sends, or whether it's momentary. | STATED (exists). Behavior: not covered | Getting Started (extra) [04:46](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=286) |
| **WHITE, BLACK(out), UV** (right side) | Full-white, blackout and UV color overrides. | STATED | Control One Getting Started [02:45](https://www.youtube.com/watch?v=eHgkltVdG-I&t=165); Getting Started (extra) [05:20](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=320) |
| **Nine color pads (center)** | Custom color overrides. Right-click one in the desktop app to change its color, and the pad LED follows. | STATED | Control One Getting Started [02:45](https://www.youtube.com/watch?v=eHgkltVdG-I&t=165); Control One x Serato DJ [04:59](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=299) |
| **Shift + color pads** | Become Position overrides, which aim the moving heads at Position Cues. | STATED | Control One Getting Started [02:45](https://www.youtube.com/watch?v=eHgkltVdG-I&t=165) |
| **Pad matrix (lower)** | Launches Autoloops, or Static Looks. | STATED | Control One Getting Started [03:20](https://www.youtube.com/watch?v=eHgkltVdG-I&t=200) |
| **Bank buttons (above the pads)** | Pick the bank. Pressing one plays that bank alone. Hold Shift to go back to playing all banks. | STATED | Control One Getting Started [03:20](https://www.youtube.com/watch?v=eHgkltVdG-I&t=200); Control One x Serato DJ [06:08](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=368) |
| **Autoloop / Static Look toggle (bottom right)** | Switches the pad matrix between Autoloop mode and Static Look mode. | STATED | Control One Getting Started [03:20](https://www.youtube.com/watch?v=eHgkltVdG-I&t=200) |
| **Touch strip** | Scales intensity. It switches between **Autoloop intensity** and **scripted-track intensity**. | STATED | Control One Getting Started [03:20](https://www.youtube.com/watch?v=eHgkltVdG-I&t=200); Control One x Serato DJ [07:11](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=431) |
| **Group buttons** | Point the touch strip at one control group, so it sets that group's intensity. One press gives Group 1 or Group 3, a double tap gives Group 2 or Group 4. That suggests two buttons with two groups each. | STATED (behavior). Two buttons: INFERRED | Control One x Serato DJ [07:11](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=431) |
| **Two DMX outs** | Two universes. The 2021 promo says 1024 channels. | STATED | Control One Getting Started [03:55](https://www.youtube.com/watch?v=eHgkltVdG-I&t=235); Introducing the Control One [00:01](https://www.youtube.com/watch?v=9a99VEkKonw&t=1) |
| **Two DMX Thru ports** | Connect a backup DMX controller or the house lighting system. When the SoundSwitch DJ disconnects, the unit switches back to the Thru source by itself. | STATED | Control One Getting Started [03:55](https://www.youtube.com/watch?v=eHgkltVdG-I&t=235), [04:25](https://www.youtube.com/watch?v=eHgkltVdG-I&t=265) |
| **Dual USB** | For handing over between DJs, or switching between a DJ's computer and a house computer running SoundSwitch standalone. | STATED | Control One Getting Started [03:55](https://www.youtube.com/watch?v=eHgkltVdG-I&t=235) |
| Promo: "pan, tilt and intensity controls" | The promo lists on-the-fly pan, tilt and intensity controls. None of the tutorials shows a pan/tilt control in use. | STATED (promo only) | Introducing the Control One (2021) [00:31](https://www.youtube.com/watch?v=9a99VEkKonw&t=31) |

**Setup facts**
- The Control One needs **SoundSwitch 2.5 or later**. STATED. Control One x Serato DJ (2021) [00:35](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=35)
- It appears in **Preferences > Hardware**, where you assign universes 1 and 2 or set it inactive. STATED. Control One Getting Started [08:14](https://www.youtube.com/watch?v=eHgkltVdG-I&t=494)
- **Patch test:** turn on the WHITE override. If every light goes white, the patch is right. Then try a color pad: any light in the wrong color, or strobing, points to a DMX patch error. STATED. Control One x Serato DJ [02:18](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=138)
- **Export to Control One** (File menu) stores one venue's data on the device. It **overwrites whatever is already stored**. Afterwards the venue shows a USB-cable icon in the Performance venue list, and selecting it *imports* the project into SoundSwitch. STATED. Control One Getting Started [06:02](https://www.youtube.com/watch?v=eHgkltVdG-I&t=362), [06:34](https://www.youtube.com/watch?v=eHgkltVdG-I&t=394), [07:09](https://www.youtube.com/watch?v=eHgkltVdG-I&t=429)
  - INFERRED: the stored copy is for a guest's computer to pick up the venue. It doesn't let the Control One run shows without a computer (see section 9, C7).

## 2. Momentary vs toggle, and LED feedback

- **Press mode** keeps an override on only while you hold the button. **Toggle mode** latches it on until you press it again. Set it per button: right-click the button in the desktop app's MIDI/Performance screen. STATED. Getting Started (2021) (extra) [03:44](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=224) and [04:15](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=255); What's New in 2.3 (extra) [02:12](https://www.youtube.com/watch?v=HSue8aJVn8c&t=132); Control One x Serato DJ [04:59](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=299)
- **Toggle is the mode for walking away.** It leaves the effect on while you go and do something else. STATED. Getting Started (extra) [04:15](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=255)
- **Pressing a latched effect again turns it off**, and you're back to the underlying show. STATED. Control One x Serato DJ [05:33](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=333)
- **The LEDs flag hidden latches.**
  - If a Static Look is on and you switch the pads back to Autoloop mode, the LEDs still show that the look is running beneath the Autoloop.
  - A Position override shows up under its color pad.
  - STATED. Control One x Serato DJ [06:08](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=368), [06:39](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=399)
- **No video gives the factory default** (press or toggle) for WHITE, BLACK, UV or SMOKE. Since the mode is set per button, Tony's BLACK toggling on a plain press could simply be how that button is set. INFERRED (see C5).

## 3. Static Looks

- **What they are:** the same as a scene in ordinary DMX software. They aren't synced to the music. They override the Autoloops and scripted tracks that are playing. STATED. Static Looks Explained (2021) [00:03](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=3) and [00:33](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=33)
- **Best uses, per the videos:** first dance, dinner service, speeches, any time the lights should sit still. At Tony's party, that's between DJs or during a toast. STATED (uses). Party mapping: INFERRED. Static Looks Explained [00:33](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=33); Getting Started (extra) [06:58](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=418)
- **They need no DJ software connection.** STATED. Getting Started (extra) [06:58](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=418)
- **Editing a look:** MIDI window > Static Looks tab. The 2021 video shows 32 buttons. Right-click > Edit. Activate a fixture so it follows the look, then set its color, intensity, gobo, position or strobe. STATED. Static Looks Explained [01:03](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=63), [02:07](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=127)
- **Layering is per fixture.** Deactivated fixtures keep following the Autoloop underneath. That holds when you change Autoloops, too: in the demo the washes stay pink while the GigBar follows each new Autoloop. STATED. Static Looks Explained [02:07](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=127), [05:15](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=315), [05:46](https://www.youtube.com/watch?v=K-wQj_oVWt8&t=346)
- **What gets overridden:** the 2021 Getting Started says the show underneath stops when a look comes on, then immediately explains that deselected fixtures keep following the Autoloop. So only the activated fixtures stop. STATED (see C6). Getting Started (extra) [07:31](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=451), [08:04](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=484)
- **Since 2.3,** looks can set every attribute per fixture, so one look can hold several colors. STATED. What's New in 2.3 (extra) [01:09](https://www.youtube.com/watch?v=HSue8aJVn8c&t=69)
- **On the Control One:** flip the pad matrix to Static Look mode, press a pad to turn a look on, and press it again to turn it off. STATED. Control One x Serato DJ [06:08](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=368)
- **Over Link,** Static Looks can be launched while synced. STATED. Ableton LINK x Serato DJ (2018) [00:42](https://www.youtube.com/watch?v=_udEdlyecGY&t=42)
- **Not covered by any video:**
  - Fades and fade times
  - The per-parameter "Thru" option
  - Running several Static Looks at once, and which one wins
  - The KB (`notes/soundswitch-kb.md`) does cover these for 2.11. The videos are silent, so trust the KB here.

## 4. Standalone mode (no DJ software)

- **The 2019 desktop route:** Performance Mode > pick the venue > MIDI menu > Standalone screen. Press **LINK** to start a show with no input from DJ software. STATED. Getting Started in Standalone Mode (2019) [00:04](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=4)
- **Setting the tempo:** click and drag the BPM display up or down, or tap the on-screen TAP (which can be MIDI-mapped). A BPM knob gives finer adjustment. STATED. Standalone Mode [00:39](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=39), [01:14](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=74)
- **When the show drifts off the beat,** use **Cue** and **Beat-shift** to bring it back into phase. STATED. Standalone Mode [00:39](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=39)
- **Launching Autoloops:**
  - Autoloops and banks launched from the Autoloops tab are **quantized to the standalone BPM**. STATED. Standalone Mode [01:14](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=74), [01:47](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=107)
  - INFERRED: a new loop starts on the beat grid, not the instant you press.
- **Live overrides** still work in standalone mode, in time with the tempo you set. STATED. Standalone Mode [01:47](https://www.youtube.com/watch?v=nd6HkCs-b0w&t=107)
- **The Control One route:** Shift + Link starts at 120 BPM, then tap BPM, and Shift + Play/Pause re-phrases. Every control behaves the same as with DJ software connected; the only difference is that you tap BPM to stay in time. STATED. Control One Getting Started [04:59](https://www.youtube.com/watch?v=eHgkltVdG-I&t=299), [06:02](https://www.youtube.com/watch?v=eHgkltVdG-I&t=362)
- **Link and standalone overlap.** In the 2019 and 2021 videos the Link button doubles as the "start standalone" button. In 2.9 the top-left **Source Selection** menu replaces this (see C2). INFERRED that Link mode, with no peer present, is the tap-tempo standalone clock. That would fit Tony's note that TAP only works in Standalone.

## 5. Tempo sources

### Ableton Link
- **Two computers on the same network.** Turn on Link in Serato (top left), then in SoundSwitch (top left). SoundSwitch syncs to Serato's timing, and moving the DJ's pitch fader changes the BPM in both. STATED. SoundSwitch x Ableton LINK x Serato DJ (2018) [00:09](https://www.youtube.com/watch?v=_udEdlyecGY&t=9)
- **While synced,** you can launch Autoloops, Static Looks ("Static Scenes") and MIDI overrides. STATED. Same video [00:42](https://www.youtube.com/watch?v=_udEdlyecGY&t=42)
- **Traktor on the same computer:** enable Link in both apps, and the Autoloops sync. STATED. SoundSwitch x Ableton LINK x Traktor Pro 2 (2018) [00:04](https://www.youtube.com/watch?v=pvLHELfYkG8&t=4)
- **Ableton Live on two computers:** activate Link in Live *and press play*, then enable Link in SoundSwitch. Timing passes across the network, and SoundSwitch follows tempo changes. STATED. SoundSwitch x Ableton LINK x Ableton Live (2018) [00:03](https://www.youtube.com/watch?v=rr5r24r6Ztw&t=3), [00:38](https://www.youtube.com/watch?v=rr5r24r6Ztw&t=38)
- **What Link carries:**
  - Tempo: STATED.
  - Beat and phase alignment: INFERRED. The videos say the loops stay in time but never mention phase.
  - Start/stop or transport: not covered. The Live demo presses play first, but no video says whether SoundSwitch follows transport.
- **Not covered by any video:**
  - What happens when the DJ hands over (one laptop leaves the Link session and another joins)
  - What happens when the DJ stops or pauses
  - Whether the upfaders or scripted tracks have any effect over Link
- **Expect, for planning (INFERRED):**
  - Link gives SoundSwitch tempo only, so no track, playhead or fader data.
  - Lights won't pause when the DJ pauses, and won't dim with the upfader. Only Autoloops will play, never scripted shows.
  - At a changeover, the tempo follows whichever Link peer changes it last. The KB adds that turning Link on disconnects SoundSwitch from the DJ software, which fits.
  - **Test this with a real guest laptop before Saturday.**
- **MIDI and Link together:** MIDI from Ableton Live can be routed into SoundSwitch, for example a drum-rack kick firing the full-white override. STATED, but only useful if a guest plays from Ableton. Ableton LINK x Ableton Live [01:46](https://www.youtube.com/watch?v=rr5r24r6Ztw&t=106), [02:22](https://www.youtube.com/watch?v=rr5r24r6Ztw&t=142); Quick Tips: MIDI Mapping with Ableton (2018) [00:03](https://www.youtube.com/watch?v=e0GvxLYS_Ro&t=3), [01:14](https://www.youtube.com/watch?v=e0GvxLYS_Ro&t=74)

### BPM Detection (2.9+) (extra video)
- **What it is:** the computer's sound card or mic detects the BPM of any audio, so Autoloops can beat-sync to a band, a club feed or an unsupported DJ setup. A **USB audio interface** gives the cleanest source. STATED. SoundSwitch 2.9 x BPM Detection (2024) [00:01](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=1)
- **Where:** Settings gear > **Tempo Detection**. Choose the audio source, the **refresh rate** (lower for changing tempos such as live bands or open format, higher for steady house), the **light show options** (Blackout, or Pause Autoloops, when audio falls below the threshold), and the **BPM range**. STATED. Same video [01:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=62), [01:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=92), [02:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=122)
- **The threshold:** drag the line on the meter to just above room noise and below the music level. Detection still runs at all levels; the threshold only drives Blackout or Pause. You can adjust it live. STATED. [02:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=152), [03:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=182)
- **Turning it on:** top-left **Source Selection** > BPM Detection > toggle. The detected BPM shows at the top left, along with the current beat of the 4-beat phrase. STATED. [02:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=152), [03:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=212)
- **Re-phasing:** to reset to beat 1, use Shift + Play/Pause on the Control One, or Standalone tab > Cue. STATED. [03:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=182)
- **Overrides** (color, strobe, others) and Static Looks all work on top. STATED. [03:32](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=212)
- **Guest playing from a phone or a non-Link app (INFERRED):** this is the source that copes with any DJ. It also has the only stated "go dark when the music stops" behavior.

### MIDI Clock / MTC in
- **Setup:** Preferences > input **MIDI sync in**, then pick the port (in the demo, a DJM-900NXS2 over USB). Many USB mixers, including Pioneer and Denon models, send MIDI clock. Otherwise you need a MIDI-to-USB interface. STATED. MIDI Clock (2021) [00:37](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=37), [01:47](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=107)
- **What it lacks:** MIDI clock "doesn't actually give us a full time signal". It only carries a tempo count, so you start the show with **Cue** and nudge with **beat shift** (Standalone screen). The BPM matches to within about 1 BPM. STATED. [02:50](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=170), [03:21](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=201), [03:51](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=231)
- **What still works:** overrides, Autoloops and white/strobe, with SoundSwitch handling the timing. STATED. [04:57](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=297)
- **History:** MIDI sync in and MIDI Clock/MTC *out* both arrived in 2.1. STATED. SoundSwitch 2.1 (2019) (extra) [02:15](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=135), [02:51](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=171)

### Virtual DJ (OS2L), including over the network
- **In VDJ:** Preferences > search "os2l" > set it to **auto**. **In SoundSwitch:** Preferences > Virtual DJ + **Auto Connect**. When it's connected, the VDJ logo turns grey at the top left. STATED. SoundSwitch X Virtual DJ (2021) [00:37](https://www.youtube.com/watch?v=pbON1Ce46OE&t=37), [01:11](https://www.youtube.com/watch?v=pbON1Ce46OE&t=71), [01:44](https://www.youtube.com/watch?v=pbON1Ce46OE&t=104)
- **Three connection options:** VDJ on **another computer by IP address**, VDJ on this computer, or **auto-connect** to the first VDJ found on the network. STATED. SoundSwitch 2.1 (2019) (extra) [04:02](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=242), [04:34](https://www.youtube.com/watch?v=8JF6C-kpLxo&t=274)
- **What VDJ drives:** pause pauses the show, scrubbing plays it forward and back, and the upfader dims the lights. STATED. SoundSwitch X Virtual DJ [02:24](https://www.youtube.com/watch?v=pbON1Ce46OE&t=144)
- **Troubleshooting:**
  - Switch VDJ's pad mode to **DMX** and press any pad to force the connection.
  - Then check the firewall. Firewall trouble is mostly a Windows issue.
  - STATED. SoundSwitch X Virtual DJ [05:04](https://www.youtube.com/watch?v=pbON1Ce46OE&t=304), [05:36](https://www.youtube.com/watch?v=pbON1Ce46OE&t=336); Virtual DJ x Control One (2021) [03:51](https://www.youtube.com/watch?v=ou90GIhgrKE&t=231)

### Serato, rekordbox, PRO DJ LINK, Engine (for guests on other setups)
- **Serato:**
  - Preferences > input Serato DJ. In Serato: Preferences > Expansion Packs > **Serato Remote**, where SoundSwitch should be listed as an active remote. If it isn't, suspect the firewall or antivirus. STATED. SoundSwitch x Serato DJ (2021) [00:35](https://www.youtube.com/watch?v=L0H2b_0_NL8&t=35), [01:08](https://www.youtube.com/watch?v=L0H2b_0_NL8&t=68)
  - The demo runs on one MacBook. No video says this works from a guest's separate laptop. INFERRED: possible, since Serato Remote is a network link, but unverified.
- **rekordbox (2026 video):** in rekordbox, Preferences > Extensions > Lighting. Turn on the Lighting function first, then enable SoundSwitch. A connection indicator in SoundSwitch confirms it. STATED. Setting up rekordbox (2026) [00:46](https://www.youtube.com/watch?v=-bThvk0XiKA&t=46)
  - The demo has rekordbox and SoundSwitch on one laptop. INFERRED: it's the same computer.
  - **Fader preferences:** the first three options set crossfader speed and curve, and "upfader-only" ignores the crossfader. STATED. [03:00](https://www.youtube.com/watch?v=-bThvk0XiKA&t=180)
- **PRO DJ LINK Bridge (2026 video):** a free AlphaTheta app for standalone CDJs (only some models are supported). In SoundSwitch: Performance mode > Source Selection > **PRO DJ LINK**, toggle on, and wait for the indicator to go green. If the Bridge runs on a separate machine, pick the network interface in SoundSwitch's PRO DJ LINK Bridge preferences. STATED. Setting up PRO DJ LINK Bridge (2026) [00:10](https://www.youtube.com/watch?v=xGAbCc1Vg9s&t=10), [02:17](https://www.youtube.com/watch?v=xGAbCc1Vg9s&t=137)
- **Engine (Denon):**
  - SoundSwitch talks to the players over **StageLinQ** (network). STATED. SoundSwitch X Engine DJ Player + Mixer (2021) [00:39](https://www.youtube.com/watch?v=ZyIc6xEljd0&t=39)
  - Engine Lighting needs a Denon X1800 or X1850 for fader data. STATED. How to setup 3 & 4 Players with Engine Lighting (2021) [00:03](https://www.youtube.com/watch?v=Z-1uj9v3zLI&t=3)
  - Engine Lighting runs Autoloops, Static Looks and scripted tracks. STATED. Getting Started with Engine Lighting (2021) [03:56](https://www.youtube.com/watch?v=FO2SDrwXtQc&t=236)
  - Only relevant if a guest brings Denon gear.
- **Fader modes** (any DJ-software source): **Blend**, **Cut** (the show changes only once the crossfader passes halfway), **Scratch** (changes only at the far ends), **Up-fader only**, and decks 1-2, 3-4 or 1-4. Pick Cut or Scratch for scratch DJs. STATED. SoundSwitch X Virtual DJ [03:00](https://www.youtube.com/watch?v=pbON1Ce46OE&t=180), [03:31](https://www.youtube.com/watch?v=pbON1Ce46OE&t=211); SoundSwitch x Serato DJ [02:14](https://www.youtube.com/watch?v=L0H2b_0_NL8&t=134), [02:44](https://www.youtube.com/watch?v=L0H2b_0_NL8&t=164)
- **Four-deck or external mixer:** map a mixer's MIDI upfaders to SoundSwitch's on-screen faders. STATED. Quick Tips: External MIDI + Four Deck Mixing (2019) [00:02](https://www.youtube.com/watch?v=9S9BGKcFic4&t=2)
- **Streamed tracks (Tidal, SoundCloud in Serato):** Autoloops sync if the beatgrid is set and the tag written; eject and reload the track. STATED. Quick Tips: Tidal + SoundCloud (2019) [00:03](https://www.youtube.com/watch?v=H7HqmVt4KGc&t=3), [00:33](https://www.youtube.com/watch?v=H7HqmVt4KGc&t=33)
- **Beatgrids matter:** Autoloops follow the DJ software's beatgrid, so a bad grid puts the lights off too. STATED. Autoloops Explained (2021) (extra) [08:31](https://www.youtube.com/watch?v=dwe6g-qczjI&t=511)

## 6. Idle: what happens when the music stops

| Situation | What the videos say | Status | Source |
|---|---|---|---|
| DJ pauses (Serato, VDJ, Engine) | The light show pauses. Scrubbing plays it forward and back. | STATED | Control One x Serato DJ [03:20](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=200); SoundSwitch X Virtual DJ [02:24](https://www.youtube.com/watch?v=pbON1Ce46OE&t=144) |
| DJ pulls the upfader down | The lights dim. | STATED | SoundSwitch X Virtual DJ [02:24](https://www.youtube.com/watch?v=pbON1Ce46OE&t=144); How to setup 3 & 4 Players with Engine Lighting [06:41](https://www.youtube.com/watch?v=Z-1uj9v3zLI&t=401) |
| Play/Pause in SoundSwitch or on the Control One | Freezes the lights in their current state. | STATED | Getting Started (extra) [04:46](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=286) |
| Paused show: lit or dark? | No video says it blacks out. INFERRED that it holds the last frame lit, which matches the steady amber Tony saw on 10-20. | INFERRED | (absence) |
| BPM Detection, audio below threshold | Blackout, or Pause Autoloops, as you choose. | STATED | 2.9 BPM Detection (extra) [02:02](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=122) |
| Link peer stops or leaves | Not covered. | - | - |
| MIDI clock stops | Not covered. Clock only carries tempo, and you start the show with Cue. | Partly STATED | MIDI Clock [02:50](https://www.youtube.com/watch?v=gRsTsb2zIRI&t=170) |
| SoundSwitch DJ unplugs from the Control One | The unit switches to whatever is on the DMX Thru ports (house system or backup controller). | STATED | Control One Getting Started [04:25](https://www.youtube.com/watch?v=eHgkltVdG-I&t=265) |
| Autoloop reaches its end | SoundSwitch launches and syncs the next Autoloop on its own. | STATED | SoundSwitch Autoloops Explained (2019) (extra) [00:38](https://www.youtube.com/watch?v=fUVeC0Hs5fw&t=38) |
| Repeat on | The current Autoloop keeps repeating until the track's audio ends. | STATED | Autoloops Explained (2021) (extra) [10:06](https://www.youtube.com/watch?v=dwe6g-qczjI&t=606) |

**Practical upshot (INFERRED):** on Link or tap tempo, nothing stops the show when the music stops. Plan on the BLACK button, a "dark" Static Look, or BPM Detection set to Blackout.

## 7. Autoloop playback in Performance mode

- **Autoloops are the fallback.** They load for any track that has no scripted show and follow the DJ software's beatgrid. Matt's own method: autoscript the key tracks and let Autoloops cover the rest, including requests. STATED. Getting Started (extra) [09:11](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=551), [10:13](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=613)
- **Controls:**
  - Next, previous, repeat, and play order (sequential or random)
  - "Override scripted tracks with Autoloops only", which Matt says to use only if you're sure
  - "Play all banks", which randomizes across every bank
  - STATED. Autoloops Explained (2021) (extra) [09:36](https://www.youtube.com/watch?v=dwe6g-qczjI&t=576), [10:06](https://www.youtube.com/watch?v=dwe6g-qczjI&t=606), [10:38](https://www.youtube.com/watch?v=dwe6g-qczjI&t=638)
- **Per-bank autoplay checkbox:** untick it and that bank never plays automatically. Use it for a strobe-heavy bank or drop-only looks that you fire by hand. STATED. Autoloops Explained (2021) [11:09](https://www.youtube.com/watch?v=dwe6g-qczjI&t=669); Scripting Session: Autoloops and MIDI (2018) [02:53](https://www.youtube.com/watch?v=WpIH8pw1z84&t=173)
- **For Tony (INFERRED):** select the genre's bank by itself (or untick autoplay on the other genre's bank), and never use "play all banks". Play-all randomizes across banks and would mix the 80s and EDM stacks.
- **Version 2.9 changes:**
  - 128 Autoloops, in 4 banks of 32.
  - In Performance mode, Autoloops can be triggered at any time, including over scripted tracks.
  - Better visual feedback on the Control One.
  - STATED. 2.9 BPM Detection (extra) [04:03](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=243), [05:03](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=303)
- **Loop Auto-Strobe** (Performance preferences) strobes automatically when the DJ applies a loop or loop roll of half a beat or less. It needs a DJ-software connection, so INFERRED: it does nothing over Link. STATED. Quick Tips: Loop Auto-Strobe (2019) (extra) [00:02](https://www.youtube.com/watch?v=xTonfl6g3AM&t=2); Getting Started (extra) [22:49](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=1369)

## 8. Live-operation tips

- **Busk on top of the running show.** Overrides stack on whatever is playing, whether an Autoloop or a scripted track. Add movement, add a color, then dial in size and speed. STATED. Getting Started (extra) [03:14](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=194); Control One x Serato DJ [03:53](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=233)
- **Use the master intensity for the room size.** The videos use it to scale output for a small or large room, or a small or large rig. STATED. Getting Started (extra) [05:51](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=351)
- **Set up group intensity first.** Assign control groups in the DMX map; then each group gets its own intensity control (touch strip + group buttons on the Control One). STATED. What's New in 2.3 (extra) [02:48](https://www.youtube.com/watch?v=HSue8aJVn8c&t=168); Control One x Serato DJ [07:11](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=431)
- **Smoke inside Autoloops.** Attribute Cues can switch smoke machines (and lasers) on, so a cue inside an Autoloop can fire the hazer. The demo turns a smoke machine on while showing an autoscripted track. STATED. This supports Tony's open item: check the Autoloops' smoke cue and set it to 0. Getting Started (extra) [15:48](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=948), [18:30](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=1110)
- **Test before guests arrive.** WHITE, then a color pad: any wrong colors or stray strobing means a patch problem. STATED. Control One x Serato DJ [02:18](https://www.youtube.com/watch?v=hiiuLxtUiqc&t=138)
- **Preview without the rig.** Art-Net can send the show to a 3D visualizer (Realizzer in the demo) on the network or the same computer. Turn it on in Preferences > General, then assign universes in the Hardware tab. STATED. Setting up SoundSwitch with a Visualizer using Art-NET (2019) [00:03](https://www.youtube.com/watch?v=JJSlRwlU5M8&t=3), [00:37](https://www.youtube.com/watch?v=JJSlRwlU5M8&t=37)
- **Check the 2.10+ license is signed in before the party.** It uses an inMusic profile, and the user account tab shows the license, sign-out and deactivation. STATED (where it lives). Pre-party check: INFERRED. SoundSwitch 2.10: New Licensing System Explained (2025) [01:32](https://www.youtube.com/watch?v=cL-XkQF9C5g&t=92)
- **Artist and interview videos** (mostly testimonials; little practical content):
  - *Eskei83* (2018): a DJ who improvises and scratches can't be followed by a light operator, and scripted lights that land on the drop solve that. STATED. [01:12](https://www.youtube.com/watch?v=SyC2oBMSwDQ&t=72)
    - Tip (INFERRED): for scratch-heavy guests, set fader mode to Cut or Scratch.
  - *Competitive Edge* (2019, a mobile lighting tech): rig and focus positions first, script very little on site, and let the upfader drive intensity. STATED. [00:04](https://www.youtube.com/watch?v=4RVHuBkONyo&t=4)
    - He aims for standout moments that make the crowd gasp. STATED. The "rather than constant busyness" reading is mine (INFERRED). [00:39](https://www.youtube.com/watch?v=4RVHuBkONyo&t=39)
  - *Ramses Ja* (2017): know your lighting the way you know your music, so you know where the lights will change. STATED. [00:00](https://www.youtube.com/watch?v=AaNeatROi4I&t=0)
  - *Mike Snell* (2020): lights synced to the music are what make a show look professional, compared with a venue operator freestyling. STATED. [00:32](https://www.youtube.com/watch?v=YsCZ7cBSmMk&t=32)
  - *Chuwe* (2017): every track carries its own show, so the set order can change freely. STATED. [00:33](https://www.youtube.com/watch?v=ptUm4BEdXCg&t=33)
  - *Mobile DJing* (2020): a testimonial only; it praises autoscript across Serato and VDJ. [00:30](https://www.youtube.com/watch?v=Nzx3lnE2y8s&t=30)
  - *DJ Spell* (2016, both videos), and *Control One for use with a Band* (2021): music or chit-chat only, nothing usable.

## 9. Contradictions and version drift

| # | Issue | Detail | Verdict |
|---|---|---|---|
| C1 | Number of Autoloops | 2019: 32 pre-built, in 4 banks of 8 ([fUVeC0Hs5fw 01:12](https://www.youtube.com/watch?v=fUVeC0Hs5fw&t=72)). 2024: 128, in 4 banks of 32 ([hj9oJqZJ55c 04:03](https://www.youtube.com/watch?v=hj9oJqZJ55c&t=243)). | Version change (2.9). The 2024 figure applies to 2.11. |
| C2 | Where Link and standalone live | 2018: a Link button at the top left. 2019: a LINK button on the Standalone screen starts a show with no DJ software. 2021: Control One Shift + TAP. 2024: a top-left **Source Selection** menu. | Version drift. On 2.11, use Source Selection or Shift + TAP. |
| C3 | Autoloops over scripted tracks | 2019 and 2021: one global "override scripted tracks" switch, to be used with care. 2.9: Autoloops can be triggered over scripted tracks at any time. | Version change. Both may still exist. |
| C4 | Control One effect row | The caption reads "movement, strobe, hue, color filter and smoke" (five). Other videos call the effect the "hue color filter" (one), and the KB lists MOVEMENT/STROBE/HUE/SMOKE. | Probably four buttons. Caption ambiguity. |
| C5 | Is BLACK momentary or toggle? | The videos say press/toggle is a per-button setting (right-click in the desktop app). Tony's KB note says the printed guide has Shift toggle WHITE/BLACK/UV, yet on his unit a plain BLACK press toggles (10-20). | Unresolved. INFERRED: his BLACK is probably set to toggle in software. Check by right-clicking BLACK in the Performance screen. |
| C6 | What a Static Look overrides | Getting Started 2021 says the show underneath stops ([07:31](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=451)), then says deselected fixtures keep following the Autoloop ([08:04](https://www.youtube.com/watch?v=8zbq-WVNN9s&t=484)). | Not a real conflict. Only the activated fixtures stop. |
| C7 | "No computer required" | The 2021 promo says no computer is needed when performing ([9a99VEkKonw 00:01](https://www.youtube.com/watch?v=9a99VEkKonw&t=1)), but that's with Engine DJ hardware. With SoundSwitch desktop, the venue stored on the Control One is *imported* into SoundSwitch on a computer ([eHgkltVdG-I 07:09](https://www.youtube.com/watch?v=eHgkltVdG-I&t=429)). The KB says it always needs a computer running 2.5+. | For Tony's setup, a computer is always needed. INFERRED from context. |
| C8 | Link alongside DJ software | The 2018 video runs Link with Serato on another machine. The KB says turning Link on disconnects SoundSwitch from the DJ software. | No conflict (INFERRED). Over Link, SoundSwitch gets only tempo from Serato, and none of Serato's track or fader data. |

## 10. Not covered by any video (test before Saturday)

1. **Link changeover:** DJ A leaves the session and DJ B joins. Does the BPM jump, hold, or drop to 120?
2. **Link stop and pause:** do the lights keep running at the last tempo, or pause?
3. **Link phase:** when a new DJ joins, do loops land on that DJ's downbeat, or do you need Shift + Play/Pause?
4. **SMOKE button:** how much it outputs, and whether it's momentary or a toggle by default.
5. **Static Look fades and Thru:** not in any video. Use the 2.11 KB notes.
6. **Default press/toggle state** of WHITE, BLACK and UV.
7. **The Control One's DMX setting (USB or Thru) in its menu.** Make sure it's on USB. (INFERRED: on Thru, the lights would follow the Thru input instead.)

## Source index (video, year, id)

| Video | Date | ID |
|---|---|---|
| Static Looks Explained | 2021-08-24 | K-wQj_oVWt8 |
| Getting Started in SoundSwitch's Standalone Mode | 2019-09-05 | nd6HkCs-b0w |
| Getting Started with the Control One | 2021-11-23 | eHgkltVdG-I |
| Control One x Serato DJ | 2021-11-23 | hiiuLxtUiqc |
| Virtual DJ x Control One | 2021-11-23 | ou90GIhgrKE |
| SoundSwitch Control One for use with a Band (music only) | 2021-11-23 | vJG--o61nF4 |
| Introducing the SoundSwitch Control One | 2021-11-23 | 9a99VEkKonw |
| SoundSwitch x Ableton LINK x Serato DJ | 2018-04-16 | _udEdlyecGY |
| SoundSwitch x Ableton LINK x Traktor Pro 2 | 2018-04-16 | pvLHELfYkG8 |
| SoundSwitch x Ableton LINK x Ableton Live | 2018-04-16 | rr5r24r6Ztw |
| MIDI Clock | 2021-08-24 | gRsTsb2zIRI |
| Quick Tips: MIDI Mapping with SoundSwitch and Ableton | 2018-05-29 | e0GvxLYS_Ro |
| Quick Tips: External MIDI + Four Deck Mixing | 2019-01-15 | 9S9BGKcFic4 |
| SoundSwitch X Virtual DJ | 2021-08-24 | pbON1Ce46OE |
| SoundSwitch x Serato DJ | 2021-08-24 | L0H2b_0_NL8 |
| SoundSwitch X Engine DJ Player + Mixer | 2021-08-24 | ZyIc6xEljd0 |
| Getting Started with Engine Lighting | 2021-10-04 | FO2SDrwXtQc |
| How to setup 3 & 4 Players with Engine Lighting | 2021-11-09 | Z-1uj9v3zLI |
| Setting up rekordbox | 2026-09-24 | -bThvk0XiKA |
| Setting up PRO DJ LINK Bridge | 2026-09-24 | xGAbCc1Vg9s |
| Setting up SoundSwitch with a Visualizer using Art-NET | 2019-09-05 | JJSlRwlU5M8 |
| Quick Tips: Tidal + SoundCloud | 2019-01-30 | H7HqmVt4KGc |
| SoundSwitch X Mobile DJing | 2020-11-19 | Nzx3lnE2y8s |
| SoundSwitch 2.10: New Licensing System Explained | 2025-06-10 | cL-XkQF9C5g |
| (extra) Getting Started | 2021-08-24 | 8zbq-WVNN9s |
| (extra) Autoloops Explained | 2021-08-24 | dwe6g-qczjI |
| (extra) SoundSwitch Autoloops Explained (Scripting Session) | 2019-09-05 | fUVeC0Hs5fw |
| (extra) Scripting Session: Autoloops and MIDI | 2018-01-16 | WpIH8pw1z84 |
| (extra) SoundSwitch 2.9 x BPM Detection | 2024-08-27 | hj9oJqZJ55c |
| (extra) What's New in SoundSwitch 2.3 | 2021-08-24 | HSue8aJVn8c |
| (extra) SoundSwitch 2.1 | 2019-09-05 | 8JF6C-kpLxo |
| (extra) Quick Tips: Autoloop Overrides | 2019-01-15 | LF548RAwFag |
| (extra) Quick Tips: Loop Auto-Strobe | 2019-01-15 | xTonfl6g3AM |
| Artist: DJ Spell (2 videos), Eskei83, Chuwe, Ramses Ja, Mike Snell, Competitive Edge | 2016-2020 | soVD2wEuCqM, BQqDXvNdRiA, SyC2oBMSwDQ, ptUm4BEdXCg, AaNeatROi4I, YsCZ7cBSmMk, 4RVHuBkONyo |
