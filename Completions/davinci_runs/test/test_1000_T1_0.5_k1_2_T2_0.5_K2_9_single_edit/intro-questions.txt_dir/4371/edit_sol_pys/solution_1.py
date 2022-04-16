#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:56:25 2020
@author: takanori
"""

s = input()

def get_min_diff(s):
    min_diff = 10000
    for i in range(len(s) - 2):
        x = int(s[i:i+3])
        diff = abs(x - 753)
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(get_min_diff(s))
