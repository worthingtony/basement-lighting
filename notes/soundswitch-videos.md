# What SoundSwitch's own videos say (read 2026-10-21)

SoundSwitch's written help is thin, and most of its knowledge base just embeds a video. So all 107 videos on the official channel were captioned and read: 95 have captions, about 50,000 words. Four topic sheets hold the details, each fact with a timestamped link and marked STATED (said in the video) or INFERRED:

- [`videos/setup-types-groups.md`](videos/setup-types-groups.md): DMX patch, fixture types, Group 1-4, fixture groups, multi-cell, venues
- [`videos/autoloops-autoscript.md`](videos/autoloops-autoscript.md): how Autoloops address fixtures, Autoscript presets, playback, idle
- [`videos/editing-techniques.md`](videos/editing-techniques.md): chases, overrides, strobe, movement, color, hot keys
- [`videos/performance-control-one-tempo.md`](videos/performance-control-one-tempo.md): Control One, Static Looks, Link, BPM Detection, VDJ
- [`videos/index.md`](videos/index.md): every video, its year and length, whether it has captions, and the KB articles that embed it

Most videos are from 2016-2021 (SoundSwitch 1.x-2.3), so menus may differ from 2.11. The raw captions are kept privately in `~/Dropbox/SoundSwitch/youtube-captions/` and aren't in this public repo.

## The answers that matter for Studio 841

**1. The three kinds of "group" are different things.**

| Setting | What it does | Changes what the loops do? |
|---|---|---|
| **Type** (Wash / Mover / Spot / Multi Cell / Strobe-Blinder / Smoke, each Primary / Secondary / Tertiary) | Autoscript reads it to decide each light's effects. Two identical washes, one Primary and one Secondary, come out of Autoscript with different effects. | Only when **Autoscript** runs, on a track or (since 2023) on an Autoloop. Hand-built loops and the Main Track ignore it. |
| **Group 1-4** (buttons in the DMX patch) | SoundSwitch calls them "control groups". They feed the Group 1-4 intensity faders in Performance mode and on the Control One's touch strip. | **No.** They're a live dimmer layer only, and Tony doesn't use them. |
| **Fixture group** (Insert > Fixture Group, the "(Group)" tracks) | Gives a group track that overrides the Main Track for its members. A chase dropped on the group spreads across them. | **Yes**, when editing: it sets what a chase or group override covers. |

What each tier (Primary, Secondary, Tertiary) actually gets isn't spelled out in any video. Each Autoscript preset has an **info (i) button** that lists what it does per fixture category, so check there in the app.

**2. Why the lights "move as one".** The stock Autoloops only drive the Main Track (except in SoundSwitch's demo venue). Every light whose own track is empty copies the Main Track. So every light gets the same intensity, color and strobe, and every mover changes position on the same beat. Type and Group 1-4 aren't the cause. Our own loops did the same thing by putting position cues on the Main Track.

**3. How SoundSwitch says to make loops dynamic.**
- **Autoscript the Autoloops** (the 2023 video). Keep the Advanced dialog open and re-apply presets until it looks right. Base Intensity sets the floor and Pulse Intensity the peak; Movement, Color Change and Effect Speed set how often things change. There are custom Primary/Secondary/Tertiary/Highlight colors. You choose which positions and attribute cues it uses and in what order. With Change & Hold on, lights hold then snap; off, they glide.
- **Split matching lights across types** (for example the left Scan 110s Mover Primary, the right ones Mover Secondary) so Autoscript gives them different effects.
- **Hand edits that break the unison:**
  - Chases across fixture tracks (Forward, Reverse, Bounce, Follow), first inside each group, then across all groups.
  - A position override per mover with staggered cues (a position chase), plus the Random Position effect.
  - Move movers in the dark, and space the moves out.
  - Intensity overrides for solo moments.
  - Strobe blocks with start and end rates on build-ups and the first bars of a drop.
  - Long color transitions instead of the built-in palettes, which change every bar.

**4. Saturday checklist** (details and sources in the performance sheet):
- **Link:** put both computers on the same network and switch Link on in the DJ's software, then in SoundSwitch. The tempo follows their pitch. **No video covers a DJ handover or stop over Link: test it with a real laptop.**
- **Pause freezes the lights lit**; it doesn't black them out. Only BPM Detection has a "below threshold, go to Blackout" option. A USB audio interface works best, with the threshold just above room noise. That's the leftover blue Tony saw at idle.
- **BPM TAP fallback:** Shift + Link (BPM TAP) starts the Autoloops at 120; tap to set the tempo, and Shift + Play/Pause brings it back onto the downbeat.
- **Bank buttons** play one bank. **Shift + bank plays all banks at random**, which would mix the 80s and EDM stacks. A per-bank autoplay switch can keep a bank manual-only.
- **Press or toggle** is set per Control One button (right-click it in the app). That's probably why BLACK toggles.
- **Static Looks** override only the lights ticked in them; everything else keeps following the Autoloop.
- **Smoke:** Attribute Cues can switch a smoke machine on, and Autoscript can place a smoke cue. Check the loops' smoke cues before Saturday, since haze is manual.

**Not covered by any video:**
- what a strobe-only fixture like the Shocker needs to fire
- the MASTER cell of a multi-cell fixture
- what Update Fixtures does to names and groups
- the exclusive bank
- Link handovers between DJs
