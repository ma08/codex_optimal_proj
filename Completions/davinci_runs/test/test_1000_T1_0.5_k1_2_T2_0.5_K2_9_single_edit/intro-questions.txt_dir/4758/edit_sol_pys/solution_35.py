
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

print(N * T * M)
