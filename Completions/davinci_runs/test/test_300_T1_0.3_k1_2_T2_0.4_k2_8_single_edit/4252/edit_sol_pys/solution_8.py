#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:46:22 2018


@author: k3sekido
"""

count = 0
for i in range(n-2):
    if s[i] == 'x' and s[i+1] == 'x' and s[i+2] == 'x':
        count += 1
print(count)
