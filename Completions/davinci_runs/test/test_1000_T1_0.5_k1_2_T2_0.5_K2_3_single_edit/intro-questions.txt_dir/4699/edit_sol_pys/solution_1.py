#!/usr/bin/env python
# -*- coding: utf-8 -*-


N = int(input())
D = set(map(int, input().split()))

# print(N, D)

for i in range(N, 10000):
    if all(d not in str(i) for d in D):
        print(i)
        break
