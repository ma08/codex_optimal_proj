#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(1000000)

c = []
for i in range(n):
    c.append((a[i]+b[i])%n)

c2 = sorted(c)

for i in range(n):
    b[c.index(c2[i])] = i

print(" ".join(map(str, b)))
