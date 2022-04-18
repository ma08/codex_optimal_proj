#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:28:09 2019
@author: yanying
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(a)
b = a[:]
for i in range(n):
    b[(i+1) % n] = a[i]
print(b)





















































