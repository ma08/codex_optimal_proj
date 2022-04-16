#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:18:03 2020

@author: yigongqin
"""



n, k = map(int, input().split())
temps = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    avg = sum(temps[i:i+k]) / k
    ans = max(ans, avg)

print(ans)
