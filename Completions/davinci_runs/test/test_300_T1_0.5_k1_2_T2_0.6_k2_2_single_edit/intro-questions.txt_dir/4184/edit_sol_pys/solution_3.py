#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 10/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

N = int(input())
W = list(map(int, input().split()))

min_diff = 100 * N
for t in range(1, N):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    diff = abs(s1 - s2)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
