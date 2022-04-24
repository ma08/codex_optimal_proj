

import sys
from math import floor, ceil

N, X = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

m_diff = max([abs(x[i] - x[i+1]) for i in range(N - 1)])

print(floor(m_diff / 2))
