#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:57:08 2020
@author: trabdlkarim
"""

n = int(input())
array = [int(i) for i in input().split()]
array.sort()

count = 0
curr = array[0]

for i in range(1, n):
    if array[i] - curr == 2:
        count += 1
        curr = array[i]

print(count, end=' ')

for i in range(1, n):
    if array[i] - curr == 2:
        print(array[i], end=' ')
        curr = array[i]
