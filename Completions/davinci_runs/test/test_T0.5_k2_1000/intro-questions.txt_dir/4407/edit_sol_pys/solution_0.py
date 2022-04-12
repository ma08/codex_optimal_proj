#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:35:31 2019

@author: hanpeng
"""

for _ in range(q):
    a = int(input())
    res = 0
    while a > 0:
        if a in coins:
            res += 1
            break
        elif a % 2 == 0:
            a = a // 2
            res += 1
        else:
            res = -1
            break
    print(res)
