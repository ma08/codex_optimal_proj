#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:57:31 2020
@author: nenad
"""

n = int(input())
a = [int(x) for x in input().split()]

contestant = []

for i in range(n):
    
    if len(contestant) == 0:
        contestant.append(a[i])
    elif a[i] <= contestant[-1] * 2:
        contestant.append(a[i])
    else:
        contestant = [a[i]]

print(len(contestant))
