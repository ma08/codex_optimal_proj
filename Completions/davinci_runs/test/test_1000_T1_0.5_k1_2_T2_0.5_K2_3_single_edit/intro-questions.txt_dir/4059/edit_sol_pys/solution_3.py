#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
N = int(input())

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        c = N - a*b
        if c > 0:
            count += 1

print(count)
