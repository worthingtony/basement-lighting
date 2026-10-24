# seq.py: the fill order, and the index of a (bank, slot) in it.
import sys
SEQ = [(1, s) for s in range(1, 33) if s != 17] + [(2, s) for s in range(1, 33)] + [(3, s) for s in range(1, 33)]
if __name__ == "__main__":
    i = int(sys.argv[1])
    print(*SEQ[i], *(SEQ[i + 1] if i + 1 < len(SEQ) else ()))
