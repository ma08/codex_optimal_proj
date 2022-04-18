
import sys

n, p, q = map(int, sys.stdin.readline().split())

if (p + q) % (2 * n) < n and (p + q) % (2 * n) > 0:
    print("paul")
else:
    print("opponent")
