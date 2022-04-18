#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] > n:
    print(-1)
    sys.exit()

s = 0
for i in range(m):
    s += a[i]

print(n - s)
