#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:23:44 2020

@author: ritambasu
"""

# SOLUTION
n = int(input())
a = list(map(int, input().split()))

# check if the array is good or not
if sum(a) - max(a) == max(a):
    print(1)
    print(a.index(max(a))+1)
else:
    print(0)

"""
Good luck!
"""
