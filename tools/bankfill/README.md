# bankfill

Scripts that filled Autoloop Banks 1-3 overnight on 2026-10-24 with the recipe Tony approved
(see `notes/stacks.md`, "Banks 1-3 filled"). They drive SoundSwitch through `tools/ui.py`.

- `build.py PHASE BANK SLOT` prints a ui.py batch: `A` opens the slot's Autoscript dialog and drags it to
  (DX,DY); `A2` fills it (preset, base 99%, slow colour, positions, custom palette); `B` applies it, drops
  the Shocker cues, renames the slot and saves. `build.py spec BANK SLOT` shows what a slot gets.
- `step.sh BANK SLOT [NEXTBANK NEXTSLOT]` finishes one slot and sets up the next.
- `run.sh N` runs N steps from `pos.txt` (an index into `seq.py`'s order) and stops on the first failure;
  `hasname.py` checks each new name in the saved project.
- `sl.py`, `openlook.py`, `white.py` drive the Static Look editor (used for the Blinder looks).
- `flow.py BANK` prints the flow order; `reorder.py BANK STATEFILE [N]` drags the bank's slots into it (STATEFILE holds the current order as original slot numbers); `renumber.py BANK` prints a batch that renames every slot to match.

Window positions are environment variables (`MX MY` main window, `DX DY` dialog). Every batch checks the
windows it expects (`expectwin`, `expectmenu`) before clicking.
