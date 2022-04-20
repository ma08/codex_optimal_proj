

import sys
import math

n, m = map(int, sys.stdin.readline().split())

prefectures = [[] for _ in range(n)]
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())
    prefectures[p-1].append(y)

for p in prefectures:
    p.sort()

for p in prefectures:
    for i, y in enumerate(p):
        print("{:06}{:06}".format(prefectures.index(p)+1, i+1))