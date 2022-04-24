#!/usr/bin/env python

import sys
from math import floor, ceil

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

X.sort()

m_diff = max([abs(X[i] - X[i+1]) for i in range(len(X) - 1)])

print(floor(m_diff / 2))
