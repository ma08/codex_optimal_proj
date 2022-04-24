#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:24:04 2018

@author: alexandreboyker
"""
n = int(input())
divisor = list(map(int, input().split()))
a = 1
b = 1
for i in range(n):
    if divisor[i] == 1:
        pass
    elif divisor[i] == divisor[i + 1]:
        a *= divisor[i]
    elif divisor[i] != divisor[i + 1]:
        b *= divisor[i]
print(a, b)
