#!/usr/bin/env python3

a, b = map(int, input().split())
m, sum = map(int, input().split())

max_rent = 0
for y in range(1, m//2 + 1):
    x = sum - 2*y
    if x >= 1:
        max_rent = max(max_rent, a*x + b*y)

print(max_rent)
