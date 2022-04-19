#!/usr/bin/env python3

import sys

k, x = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    print(x - k + 1 + i, end=" ")
