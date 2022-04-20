#!/usr/bin/env python3

n = int(input())
heights = list(map(int, input().split()))

for i in range(1, n):
    if heights[i] < heights[i - 1]:
        heights[i] = heights[i - 1]

print('Yes')
