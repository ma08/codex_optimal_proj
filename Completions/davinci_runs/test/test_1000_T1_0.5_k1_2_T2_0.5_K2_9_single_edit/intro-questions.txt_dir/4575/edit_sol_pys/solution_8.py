#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:08:55 2019

@author: xsxsz
"""


n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

for i in range(n):
    x += (d-1) // a[i] + 1

print(x)
