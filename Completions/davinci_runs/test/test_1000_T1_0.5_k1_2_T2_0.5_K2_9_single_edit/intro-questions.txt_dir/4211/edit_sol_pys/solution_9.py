#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:54:38 2020


@author: suryakantkumar
"""

a = []

for i in range(n-1):
    if b[i] <= b[i+1]:
        a.append(b[i])
    else:
        a.append(b[i+1])

a.append(b[n-2])

print(sum(a))
