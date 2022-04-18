#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:06:09 2019
@author: duynguyen
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 1
r = 10**9

while l <= r:
    m = (l+r)//2

    if sum(1 for x in a if x <= m) >= k:
        r = m-1
    else:
        l = m+1

if sum(1 for x in a if x <= l) == k:
    print(l)
else:
    print(-1)
