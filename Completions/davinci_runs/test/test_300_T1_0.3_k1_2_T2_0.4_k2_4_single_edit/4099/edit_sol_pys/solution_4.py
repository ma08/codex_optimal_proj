# -*- coding: utf-8 -*-

import sys

n, k, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

if sum(a) / (n-1) >= m:
    print(-1)
else:
    print(m*n - sum(a))
