import sys
n, p, q = map(int, sys.stdin.readline().split())

if (p + q) % (2 * n) <= n:
    print("paul")
else:
    print("opponent")
