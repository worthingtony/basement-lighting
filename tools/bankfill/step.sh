#!/bin/zsh
# step.sh BANK SLOT [NEXTBANK NEXTSLOT]: finish BANK/SLOT (apply, cues, rename, save), then open + fill the next one.
S=${0:A:h}
cd $S/../.. || exit 1
export MX=${MX:-0} MY=${MY:-126} DX=${DX:-0} DY=${DY:-300}
{ python3 -I $S/build.py B $1 $2; if [ -n "$3" ]; then python3 -I $S/build.py A $3 $4 && python3 -I $S/build.py A2 $3 $4; fi; } > $S/step.txt || exit 1
python3 -I tools/ui.py --app SoundSwitch batch $S/step.txt > $S/step.log 2>&1
rc=$?; echo "exit $rc"; [ $rc -ne 0 ] && tail -3 $S/step.log
[ -n "$3" ] && python3 -I $S/build.py spec $3 $4
