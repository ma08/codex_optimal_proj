#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:50:41 2019

@author: filipe
"""


n, m = map(int, input().split())

left = [0] * (m + 1)
right = [0] * (m + 1)

for i in range(n):
    l, r = map(int, input().split())
    left[l] += 1
    right[r] += 1

counter = 0
for i in range(1, m + 1):
    if left[i] == right[i]:
        counter += 1
    elif left[i] > right[i]:
        print(counter)
        break
else:
    print(counter)
