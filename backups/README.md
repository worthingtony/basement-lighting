# Backups

Copies of the SoundSwitch project and the custom Fixture Manager profiles, so a lost Mac or a bad Update Fixtures can be undone. All of these files are binary or encrypted: they can be restored, not read or diffed.

| Path | What | Taken |
|---|---|---|
| `soundswitch/Claude-2100.ssproj/` | The newest project, copied from `~/Dropbox/SoundSwitch/`. Includes changes saved on 2026-10-12/13 (Autoloops 21-22, venues, track map). The two Dropbox "conflicted copy" files are left out. | 2026-10-20, before the Scan 110 and Vortex profiles |
| `fixture-profiles/*.plfix` | Each custom profile, exported with Fixture Manager > File > Save Fixture As | 2026-10-20 |

## Restoring
- **Project:** copy the `.ssproj` folder back into `~/Dropbox/SoundSwitch/` under a new name, then open it in SoundSwitch.
- **Profile:** Fixture Manager > File > Open Fixture, pick the `.plfix`, then File > Save Workspace. Then Options > Update Fixtures in SoundSwitch (save the project first).

## Not here
- **Fixture Manager's workspace** (`~/Library/Application Support/inMusicBrands/FixtureLibrary/Workspace.db`, encrypted) is kept out of this public repo, since its contents can't be checked. A pre-change copy is in `~/Dropbox/SoundSwitch/backup-2026-10-20/`.
