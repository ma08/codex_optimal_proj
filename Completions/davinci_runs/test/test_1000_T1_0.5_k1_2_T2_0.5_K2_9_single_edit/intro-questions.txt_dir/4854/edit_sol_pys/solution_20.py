#!/usr/bin/env python
# coding: utf-8

import sys

n, c = map(int, sys.stdin.readline().split())

message = list(map(int, sys.stdin.readline().split()))

freq = [0] * (c + 1)

for i in message:
    freq[i] += 1

for i, c in enumerate(freq):
    if c > 0:
        print(str(i) * c, end=' ')
