#!/usr/bin/env python3
a, b = map(int, input().split())
m, sigma = map(float, input().split())

if sigma <= 2:
    print(int(a*m))
else:
    y = (sigma - 2) / 3
    x = m - y
    print(int(a*x + b*y))
