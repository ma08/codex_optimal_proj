#!/usr/bin/env python3

a, b = map(int, input().split())

if a % b == 0:
    print(a + b)
else:
    print(b - a)
