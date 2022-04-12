#!/usr/bin/env python3

n = int(input())
h = list(map(int, input().split()))
h.sort()

if h[0] == 0:
    print("impossible")
else:
    print(h[0] / n)
