#!/usr/bin/env python3

import sys

N, K = map(int, sys.stdin.readline().rstrip().split()) # N is the number of items, K is the number of items to buy

prices = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

total = 0
for i in range(K):
    total += prices[i]

print(total)
