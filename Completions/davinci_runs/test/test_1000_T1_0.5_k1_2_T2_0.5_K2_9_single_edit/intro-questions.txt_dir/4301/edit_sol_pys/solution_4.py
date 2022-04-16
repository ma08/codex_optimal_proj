#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:39:17 2020

@author: karanwaghela
"""

n = int(input())
arr = [int(input()) for _ in range(n)]
max_arr = max(arr)
print(*[max_arr if x == max_arr else max_arr-1 for x in arr])
