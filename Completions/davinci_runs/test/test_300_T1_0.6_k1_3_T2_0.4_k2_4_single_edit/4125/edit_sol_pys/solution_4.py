
import sys
from math import floor

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

x.sort()

m_diff = max([abs(x[i] - x[i+1]) for i in range(len(x) - 1)])

print(floor(m_diff / 2))
