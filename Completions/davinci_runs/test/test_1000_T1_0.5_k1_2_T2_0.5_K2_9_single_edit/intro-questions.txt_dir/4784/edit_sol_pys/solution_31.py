#!/usr/bin/env python3

x = int(input())
n = int(input())

res = x
for i in range(n):
    res += x - int(input())

print(res)
