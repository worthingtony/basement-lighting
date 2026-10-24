# flow.py BANK: the flow order for a bank, as original slot numbers (= the number in each loop's name).
# Each run of 8 walks a colour chain where neighbours share a hue. Which copy of each palette goes in
# which run is searched so that neighbours never share a preset or a position order.
import random, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from build import PRESETS, spec
CHAIN = {1: [6, 2, 0, 4, 5, 1, 7, 3],   # Cyan Blue, Teal Magenta, Blue Magenta, Violet Pink, Amber Magenta, Amber Blue, Red White, Blue Warm
         2: [1, 7, 3, 4, 2, 6, 5, 0],   # Miami, Lavender Teal, Purple Gold, Pink Yellow, Sunset, Red Blue, Electric Blue, Neon Pink Cyan
         3: [0, 3, 7, 6, 2, 4, 5, 1]}   # Red White, Gold White, Orange Teal, Pink Cyan, Magenta Red, UV Purple, Blue Red, Ice Blue

def preset(bank, src):
    return "AS" if (bank, src) == (1, 17) else spec(bank, src)["preset"]

def seq(bank, var):  # var[c] = the variant (copy) of palette c used in runs 0..3
    return [var[c][k] * 8 + c + 1 for k in range(4) for c in CHAIN[bank]]

def cost(bank, o):
    pr = [preset(bank, s) for s in o]
    va = [(s - 1) // 8 for s in o]
    n = 0
    for i in range(1, 32):
        n += 10 * (pr[i] == pr[i - 1]) + 3 * (va[i] == va[i - 1])
        if i > 1:
            n += pr[i] == pr[i - 2]
    return n

def order(bank, seed=841):
    rnd = random.Random(seed)
    best = None
    for _ in range(40):
        var = {c: rnd.sample(range(4), 4) for c in range(8)}
        cur = cost(bank, seq(bank, var))
        for _ in range(3000):
            c = rnd.randrange(8); a, b = rnd.sample(range(4), 2)
            var[c][a], var[c][b] = var[c][b], var[c][a]
            new = cost(bank, seq(bank, var))
            if new <= cur:
                cur = new
            else:
                var[c][a], var[c][b] = var[c][b], var[c][a]
        if best is None or cur < best[0]:
            best = (cur, seq(bank, var))
    return best[1]

if __name__ == "__main__":
    b = int(sys.argv[1])
    o = order(b)
    assert sorted(o) == list(range(1, 33))
    print("cost", cost(b, o))
    for p, src in enumerate(o, 1):
        s = spec(b, src)
        name = "AS Test Tech House" if (b, src) == (1, 17) else s["name"]
        print(f"{p:2d} <- {src:2d} {name:22s} {preset(b, src):7s} v{(src - 1) // 8 + 1}")
