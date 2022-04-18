
import sys
n, p, q = map(int, input().split())

if p == q:
    print("paul")
    sys.exit()

if (q - p) % (2 * n) <= n:
    print("paul")
else:
    print("opponent")
