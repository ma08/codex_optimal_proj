# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:03:05 2019

@author: Administrator
"""


n = int(input())
a = list(map(int, input().split())) 

for i in range(n):
    print(sum(abs(a[j] - a[i]) for j in range(n) if j != i))
