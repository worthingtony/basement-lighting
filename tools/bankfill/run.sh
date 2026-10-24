#!/bin/zsh
# run.sh N: do N steps from the position in pos.txt (index into seq.py's SEQ of the slot whose dialog is open).
S=${0:A:h}
for k in $(seq 1 $1); do
  i=$(cat $S/pos.txt)
  set -- $(python3 -I $S/seq.py $i)
  t0=$(date +%s)
  out=$(zsh $S/step.sh $@); rc=$?
  name=$(python3 -I $S/build.py spec $1 $2 | python3 -I -c "import sys,ast; print(ast.literal_eval(sys.stdin.read())['name'])")
  echo "[$(date +%H:%M:%S)] bank $1 slot $2 '$name': $(echo $out | head -1) ($(( $(date +%s) - t0 ))s)"
  if ! echo "$out" | head -1 | grep -q "exit 0"; then echo "$out"; exit 1; fi
  python3 -I $S/hasname.py "$name" || { echo "NAME NOT SAVED: $name"; exit 1; }
  echo $((i + 1)) > $S/pos.txt
  [ -z "$3" ] && { echo "SEQUENCE DONE"; exit 0; }
  echo "  next: $3 $4 $(echo "$out" | tail -1)"
done
