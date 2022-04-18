#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:37:51 2020
"""

# SOLUTION
q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    if n == 1:
        print("YES")
        continue
    if n == 2:
        if p[0] == 1 and p[1] == 2:
            print("YES")
        else:
            print("NO")
        continue
    if p[0] == 1:
        start = 1
        if p[1] == 2:
            direction = 1
        else:
            direction = -1
    else:
        start = p.index(1)
        if p[start - 1] == n:
            direction = 1
        else:
            direction = -1
    for i in range(n):
        if p[(start + direction * i) % n] != (i + 1) % n + 1:
            print("NO")
            break
    else:
        print("YES")
