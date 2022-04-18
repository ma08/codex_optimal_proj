

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

B = [0] * N

for i in range(N):
    B[A[i]-1] = i + 1

for i in range(N):
    print(B[i])
