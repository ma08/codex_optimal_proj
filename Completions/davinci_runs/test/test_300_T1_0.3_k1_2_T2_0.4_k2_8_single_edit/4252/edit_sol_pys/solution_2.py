#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:13:40 2019


@author: abhijithneilabraham
"""

count = 0
for i in range(n-2):
    if s[i] == 'x' and s[i+1] == 'x' and s[i+2] == 'x':
        count += 1
print(count)
