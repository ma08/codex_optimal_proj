

import sys

# input
N, K, Q = map(int,sys.stdin.readline().split())
A = []
for i in range(Q):
    A.append(int(sys.stdin.readline()))

# initialization
scores = [K] * N

# main
for i in range(Q):
    scores[A[i]-1] -= 1
    if scores[A[i]-1] <= 0:
        scores[A[i]-1] = 0

# output
for i in range(N):
    if scores[i] > 0:
        print("Yes")
    else:
        print("No")