

import sys

H, n = [int(x) for x in sys.stdin.readline().split()]
d = [int(x) for x in sys.stdin.readline().split()]

h = H
for i in range(n):
    h += d[i]
    if h <= 0:
        print(i+1)
        break
else:
    print(-1)