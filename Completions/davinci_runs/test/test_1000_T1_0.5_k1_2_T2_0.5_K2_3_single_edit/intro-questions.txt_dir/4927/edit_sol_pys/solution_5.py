
import sys
sys.setrecursionlimit(10000)


def solve(n, p, q):

if (p + q) % (2 * n) < n:
    print("paul")
else:
    print("opponent")
