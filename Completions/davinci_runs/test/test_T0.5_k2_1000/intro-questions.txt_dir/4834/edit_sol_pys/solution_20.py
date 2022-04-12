#!/usr/bin/env python3

import sys

n = int(input())
teams = [int(x) for x in sys.stdin.readline().split()]

teams = sorted(teams)

total_time = 0

for i in range(n):
    total_time += teams[i] * (n - i)

print(total_time)
