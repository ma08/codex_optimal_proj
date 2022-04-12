#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:05:14 2019

@author: y56
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

a_sum = sum(a)
b_sum = sum(b)

a_max = a[-1]
b_max = b[-1]

if a_max > b_max:
    print(-1)
    exit()

if a_sum > b_sum:
    print(-1)
    exit()

if a_max == b_max:
    print(0)
    exit()

a_max_cnt = a.count(a_max)
b_max_cnt = b.count(b_max)

a_max_cnt = a_max_cnt - (a_sum - b_sum) // (b_max - a_max)

if a_max_cnt <= 0:
    print(0)
    exit()

print(a_max_cnt)
