
from sys import stdin

N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

for i in range(K):
    B = [0] * N
    for j in range(N):
        if j - A[j] >= 0:
            B[j - A[j]] += 1
        if j + A[j] < N:
            B[j + A[j]] += 1
    A = B
for i in A:
    print(i)
