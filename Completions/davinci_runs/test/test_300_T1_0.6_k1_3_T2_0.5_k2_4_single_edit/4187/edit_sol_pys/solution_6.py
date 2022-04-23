#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:30:54 2020

@author: antonio
"""
#%%

n = int(input())
a = list(map(int, input().split()))
a.append(a[0])
a.append(a[1])

best = 0
length = 0

for i in range(n + 2):
    if a[i] == 1:
        length += 1
    else:
        best = max(best, length)
        length = 0

#%%
print(best)
