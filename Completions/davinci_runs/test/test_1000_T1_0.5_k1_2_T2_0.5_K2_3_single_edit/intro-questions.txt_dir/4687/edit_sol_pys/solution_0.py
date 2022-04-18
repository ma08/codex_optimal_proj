
import sys

N, K = map(int, input().split())

A = [0 for i in range(N)]
B = [0 for i in range(N)]

for i in range(N): 
    A[i], B[i] = map(int, input().split())

A = sorted(A)
B = sorted(B)

if K <= B[N - 1]:
    print(A[K - 1])
else:
    print(A[N - 1])
