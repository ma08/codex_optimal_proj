
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:14:56 2020
@author: nenad
"""
def hailstone_sum(n, acc=0):
    # base case
    if n == 1: return acc + 1
    # recursive case
    elif n % 2 == 0: return hailstone_sum(n // 2, acc + n)
    else: return hailstone_sum(3*n + 1, acc + n)
    
n = int(input())    
print(hailstone_sum(n))    
