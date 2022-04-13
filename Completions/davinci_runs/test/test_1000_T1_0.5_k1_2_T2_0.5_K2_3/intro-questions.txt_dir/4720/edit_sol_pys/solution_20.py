#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:59:23 2018

@author: j
"""

N = int(input())
count = 0
seats = [0 for i in range(100000)]
for i in range(N):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        seats[j-1] += 1
for i in range(len(seats)):
    if seats[i] > 0:
        count += 1
print(count)
