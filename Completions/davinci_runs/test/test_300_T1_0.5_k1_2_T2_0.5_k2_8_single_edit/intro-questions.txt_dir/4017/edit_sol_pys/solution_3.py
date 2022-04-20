#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import random

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split(' '))

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)
