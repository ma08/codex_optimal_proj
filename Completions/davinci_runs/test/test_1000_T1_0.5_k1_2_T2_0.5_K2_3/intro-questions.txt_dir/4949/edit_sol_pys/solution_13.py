#!/usr/bin/env python3


import sys

n, w, h = map(int, input().split())

for i in range(n):
    x, y = map(int, input().split())
    if x <= w or y <= h:
        print("DA")
    else:
        print("NE")
