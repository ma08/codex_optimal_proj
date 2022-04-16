#!/usr/bin/env python
# coding: utf-8

import sys

k, x = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    print(x - k + 1 + i, end=" ")
