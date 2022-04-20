

import sys

N = int(sys.stdin.readline())
B = [int(i) for i in sys.stdin.readline().split()]

A = [0]*N

A[0] = B[0]
A[-1] = B[-1]

for i in range(1, N-1):
    A[i] = min(B[i], A[i-1])

print(sum(A))