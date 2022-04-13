#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:12:30 2019
@author: robert
"""

n = int(input())
c = [int(x) for x in input().split()]

c.sort()

if c[-1] > n:
    print("impossible")
else:
    m = 0
    for i in range(n-1, -1, -1):
        if c[i] > m + 1:
            m += 1
        else:
            break
    print(m)
