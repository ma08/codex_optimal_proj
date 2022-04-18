# -*- coding: utf-8 -*-

import sys

N, K = map(int,sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))[:N]

count = 0
for i in range(N):
    if h[i] >= K:
        count += 1

print(count)
