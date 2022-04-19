#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:44:44 2020


@author: nenad
"""

def count_set_bits(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count
    
def count_set_bits_2(x):
    count = 0
    while x:
        count += 1
        x &= (x-1)
    return count


print(count)
