

import sys

def get_diff(x):
    return max([abs(x[i] - x[i+1]) for i in range(len(x) - 1)])
from math import floor, ceil

N, X = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

m_diff = get_diff(x)

if m_diff % 2 == 0:
    if m_diff // 2 < X:
        print(m_diff // 2)
        exit()
    else:
        print(X)
        exit()

print(floor(m_diff / 2))
