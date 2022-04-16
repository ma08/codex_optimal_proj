#!/usr/bin/env python3

from itertools import product

b, d, c, l = map(int, input().split())

for i, j, k in product(range(l//b + 1), range(l//d + 1), range(l//c + 1)):
    if i*b + j*d + k*c == l and i*b > 0 and j*d > 0 and k*c > 0:
        print(i, j, k, sep=" ")
