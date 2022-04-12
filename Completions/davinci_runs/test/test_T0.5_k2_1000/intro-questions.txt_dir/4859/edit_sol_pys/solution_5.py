#!/usr/bin/env python3

from itertools import product

a, b, c, l = map(int, input().split())

for i, j, k in product(range(l // a + 1), range(l // b + 1), range(l // c + 1)):
    if i * a + j * b + k * c == l:
        print(i, j, k, sep=' ')
