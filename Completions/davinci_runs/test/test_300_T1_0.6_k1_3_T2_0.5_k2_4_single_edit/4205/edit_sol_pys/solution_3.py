#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:31:03 2020


@author: tarun.bhavnani@dev.smecorner.com
"""

p_sorted = sorted(p)

for i in range(N):
    if p[i] == p_sorted[i]:
        continue
    else:
        p[i], p[p.index(p_sorted[i])] = p[p.index(p_sorted[i])], p[i]
        if p == p_sorted:
            print("YES")
            exit()

print("NO")
