#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:29:56 2020
@author: suryakantkumar
"""

n = int(input())

l = list(map(int, input().split()))

if max(l) < sum(l)-max(l):
    print("Yes")
else:
    print("No")
