#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:46:27 2020
@author: piumallick
"""

n = int(input())
s = input()

counts = [0, 0]
for i in range(n):
    counts[0 if s[i] == '(' else 1] += 1

if counts[0] != counts[1]:
    print(0)
else:
    print(n // 2)
