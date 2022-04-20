# -*- coding: utf-8 -*-

import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split())

if n * a <= b:
    print(n * a)
else:
    print(b)
