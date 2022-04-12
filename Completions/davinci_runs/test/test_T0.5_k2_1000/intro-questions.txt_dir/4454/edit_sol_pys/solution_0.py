#!/usr/bin/env python3

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) // n + (sum(a) % n > 0))
