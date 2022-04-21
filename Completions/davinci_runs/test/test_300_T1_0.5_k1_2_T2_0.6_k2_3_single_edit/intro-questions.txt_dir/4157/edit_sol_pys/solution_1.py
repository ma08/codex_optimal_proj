#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

b = []

for i in range(n):
    if a and (not b or b[-1]*2 > a[0]):
        b.append(a.pop(0))
    else:
        b.append(b.pop(0)*2)

print(' '.join(map(str, b)))
