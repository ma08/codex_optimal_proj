# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:51:21 2020
@author: yuya
"""

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1
print(count)
