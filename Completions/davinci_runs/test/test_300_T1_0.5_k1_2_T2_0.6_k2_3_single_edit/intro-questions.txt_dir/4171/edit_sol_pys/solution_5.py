#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:33:00 2019

@author: karips

Problem:

"""

# Solution

n,k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1: print(max(a))
else: print(max(a)-min(a)+1)
