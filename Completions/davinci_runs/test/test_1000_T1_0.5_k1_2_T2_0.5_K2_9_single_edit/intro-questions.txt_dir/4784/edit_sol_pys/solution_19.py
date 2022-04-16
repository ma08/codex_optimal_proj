#!/usr/bin/env python3

x = int(input())
n = int(input())

p = [0] * n
for i in range(n):
    p[i] = int(input())

print(x - sum(p))
