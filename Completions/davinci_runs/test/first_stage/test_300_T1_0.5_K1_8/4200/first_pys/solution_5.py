

import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

if A[N-M] >= (sum(A) / (4 * M)):
    print("Yes")
else:
    print("No")