

import sys

n, x = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))
d = 0
c = 0

for i in range(n):
    d += l[i]
    if d <= x:
        c += 1

print(c + 1)
