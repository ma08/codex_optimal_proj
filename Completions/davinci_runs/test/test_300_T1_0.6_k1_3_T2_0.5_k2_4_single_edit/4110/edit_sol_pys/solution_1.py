# coding: utf-8

import sys

d, g = list(map(int, sys.stdin.readline().split()))
p_c = []
for _ in range(d):
    p_c.append(tuple(map(int, sys.stdin.readline().split())))

n = 0
p_c = sorted(p_c, key=lambda x: x[1])
for i, (p, c) in enumerate(p_c):
    if g >= c * (i + 1):
        n += p
        g -= c * (i + 1)
        break
    else:
        n += p
        g -= p * 100

if g > 0:
    n += (g + 99) // 100

print(n)
