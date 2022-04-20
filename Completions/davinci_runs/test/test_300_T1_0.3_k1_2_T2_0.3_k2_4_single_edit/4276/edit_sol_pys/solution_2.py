#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:10:07 2020

@author: kudevara
"""

N, T = map(int, input().split())
costs = []
times = []
for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = sorted(costs)
times = sorted(times)

if times[0] > T:
    print("TLE")
else:
    print(costs[0])
