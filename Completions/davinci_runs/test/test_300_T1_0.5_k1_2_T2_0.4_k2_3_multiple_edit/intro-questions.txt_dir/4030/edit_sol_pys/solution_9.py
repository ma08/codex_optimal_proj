#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:05:33 2020
@author: nenad
"""

n = int(input())
s = input()

if n == 1:
    print(1)
    print(1)
    exit()

if n == 2:
    print(2)
    print(1, 2)
    exit()

c = [1] * (n + 1)

for i in range(1, n):
    if s[i] > s[i - 1]:
        c[i] = c[i - 1] + 1

for i in range(n - 2, -1, -1):
    if s[i] > s[i + 1]:
        c[i] = max(c[i], c[i + 1] + 1)

print(c[n - 1])
print(*c[:n])
