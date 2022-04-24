#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:09:32 2020


@author: nenad
"""

count = 0

for i in range(1, n - 1):
    if a[i - 1] == a[i + 1] == 1:
        count += 1

print(count)
