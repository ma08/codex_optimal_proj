#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:19:57 2019

@author: yoshinonakanishi
"""


s = input()
t = input()

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
