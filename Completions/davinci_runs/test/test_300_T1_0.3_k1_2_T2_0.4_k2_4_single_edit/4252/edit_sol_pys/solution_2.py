#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:44:26 2020


@author: abhijithneilabraham
"""

count = 0
for i in range(n-2):
    if s[i] == s[i+1] == s[i+2] == "x":
        count += 1

print(count)
