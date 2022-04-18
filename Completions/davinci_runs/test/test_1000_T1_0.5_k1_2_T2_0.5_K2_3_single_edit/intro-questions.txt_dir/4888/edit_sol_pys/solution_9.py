#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:33:13 2020

@author: nenad
"""

n, T = map(int, input().split())
times = list(map(int, input().split()))

curr_time = 0
num_tasks = 0

for i in range(n):
    if curr_time + times[i] <= T:
        num_tasks += 1
        curr_time += times[i]
    else:
        break

print(num_tasks)
