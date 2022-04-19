#!/usr/bin/env python3

# a = bottle 1, b = bottle 2
a, b, c = map(int, input().split())

if b + c > a:
    print(b + c - a)
else:
    print(0)
