

import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

if N < sum(A):
    print(-1)
else:
    print(N - sum(A))