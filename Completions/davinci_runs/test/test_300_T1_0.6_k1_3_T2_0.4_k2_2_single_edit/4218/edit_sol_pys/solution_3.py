#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:51:46 2019
@author: abhijithneilabraham
"""

N = int(input())

odd = 0
for i in range(1, N+1):
    if i % 2 != 0:
        odd += 1

print(odd/N)
