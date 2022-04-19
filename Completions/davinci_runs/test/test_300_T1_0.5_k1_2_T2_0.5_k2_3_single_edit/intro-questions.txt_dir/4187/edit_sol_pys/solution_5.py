#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:50:08 2020

@author: kathykiutang
"""

n = int(input())
a = list(map(int, input().split()))

max_rest = 0
rest = 0

for i in a:
    if i == 0:
        max_rest = max(max_rest, rest)
        rest = 0
    else:
        rest += 1

max_rest = max(max_rest, rest)
print(max_rest)
