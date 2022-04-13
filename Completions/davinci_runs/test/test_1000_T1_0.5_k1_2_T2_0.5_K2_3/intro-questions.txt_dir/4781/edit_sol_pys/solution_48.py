#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:01:52 2018
"""
k = int(input())
n = int(input())

for i in range(n):
    t, z = input().split()
    t = int(t)
    if (t + k) % 8 == 0:
        k = 8
    else:
        k = (t + k) % 8

print(k)
