#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:43:14 2019
@author: abhijithneilabraham
"""

from collections import Counter
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    p.append(n)
    d = Counter()
    c = 0
    for i in range(n):
        if i == p[c]:
            c += 1
        d[s[i]] += n - p[c]
    print(*d.values())
