
import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
h = defaultdict(list)
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    h[x].append(y)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a in h:
        h[a].append(b)
    else:
        h[a] = [b]
for i in sorted(h.keys()):
    for j in sorted(h[i]):
        print(i, j)
