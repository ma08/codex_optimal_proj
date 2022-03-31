#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:23:57 2018
@author: raja
"""

n = int(input())
a = list(map(int, input().split()))
a_sum = sum(a)
res = []
for i in range(n):
    if a[i] == a_sum - a[i]:
        res.append(i + 1)
print(len(res))
if len(res) > 0:
    print(*res)
