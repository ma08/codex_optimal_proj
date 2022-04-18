#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:18:54 2018
"""

n = int(input())
arr = [int(x) for x in input().split()]

curr_min = min(arr)
curr_max = max(arr)

print(curr_max - curr_min - 2 * min(curr_max - curr_min, min(arr.count(curr_min), arr.count(curr_max))))
