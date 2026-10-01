"""Erdős #338, HHP block model (exact rational arithmetic, small).

Block B(x) = [x, x + x^2] U {x + c x^2 : c in C}, C a finite set of reals > 1.  In units of x^2 (dropping the j*x offsets),
a sum of at most h elements is  sigma(S) + u  with S a multiset of C, |S| <= h, 0 <= u <= h - |S|  (u from the interval part).
reach(C, h)   = right end of the connected component of 0 in  U_S [sigma(S), sigma(S) + h - |S|]   (S multisets, |S| <= h)
rreach(C, l)  = the same with S a SUBSET of C (distinct elements) and at most l summands in total.
lstar(C, h)   = least l with rreach(C, l) >= reach(C, h)   (the block's restricted order in this model).
"""
from fractions import Fraction as Fr
from itertools import combinations_with_replacement, combinations
import sys

def component_end(intervals):
    """right end of the connected component of 0 in a union of closed intervals"""
    end = Fr(0); progress = True
    iv = sorted(intervals)
    while progress:
        progress = False
        for a, b in iv:
            if a <= end < b: end = b; progress = True
    return end

def reach(C, h):
    iv = []
    for k in range(0, h + 1):
        for S in combinations_with_replacement(C, k):
            s = sum(S, Fr(0)); iv.append((s, s + h - k))
    return component_end(iv)

def rreach(C, l):
    iv = []
    for k in range(0, min(l, len(C)) + 1):
        for T in combinations(C, k):
            s = sum(T, Fr(0)); iv.append((s, s + l - k))
    return component_end(iv)

def lstar(C, h):
    R = reach(C, h); l = h
    while rreach(C, l) < R: l += 1
    return l, R

if __name__ == "__main__":
    import random
    from itertools import combinations
    # 1. HHP's sets C = {2, 4, ..., 2^(h-2)} (elements c <= 1 add nothing in the model): expected 2^(h-2) + h - 1
    for h in (3, 4, 5, 6):
        C = [Fr(2 ** i) for i in range(1, h - 1)]
        l, R = lstar(C, h)
        print(f"HHP h={h} C={[str(c) for c in C]}: reach {R}, lstar {l} (expected {2 ** (h - 2) + h - 1})", flush=True)
    # 2. Bitter Lemma's value 9 at h = 4 with |C| = 2 (C_max = 16, sum C = 9), and a search over |C| <= 3 on a grid of halves
    l, R = lstar([Fr(4), Fr(5)], 4)
    print(f"h=4 C=['4','5']: reach {R}, lstar {l}", flush=True)
    grid = [Fr(k, 2) for k in range(3, 33)]
    for m in (1, 2, 3):
        best = max((lstar(list(C), 4)[0], [str(c) for c in C]) for C in combinations(grid, m))
        print(f"h=4 grid search |C|={m}: max lstar {best[0]} at {best[1]}", flush=True)
    # 3. Theorem 2 sanity check: random C (up to 6 elements, rationals with denominator 10 in (1, 12]) at h = 3
    rnd = random.Random(7); mx = 0
    for _ in range(4000):
        C = sorted({Fr(rnd.randint(11, 120), 10) for _ in range(rnd.randint(1, 6))})
        mx = max(mx, lstar(C, 3)[0])
    print(f"h=3 random check, 4000 sets: max lstar {mx} (Theorem 2: at most 4)", flush=True)
