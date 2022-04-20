#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:40:22 2020
@author: alex
"""

k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + '...')
