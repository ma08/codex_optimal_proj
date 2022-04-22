

import sys

n, x = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))[:n]

d = 0
cnt = 0

for i in range(n):
    d += l[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
