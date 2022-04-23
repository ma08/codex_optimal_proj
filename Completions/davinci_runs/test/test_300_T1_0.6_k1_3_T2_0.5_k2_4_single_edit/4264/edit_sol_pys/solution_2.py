#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:48:23 2020
@author: kenkuo
"""

N = int(input())

if N < 1 or N > 10 ** 5:
    print("invalid input, must be 1 <= N <= 10^5")

# 9, 99, 999, 9999, 99999, ...
length = len(str(N))

# 1, 3, 5, 7, 9, ...
if length % 2 == 1:
    ans = 10 ** (length // 2)
else:
    ans = 10 ** (length // 2) + N - 10 ** (length - 1)

print(ans)
