
import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            C[i] += 1
for i in range(N):
    print(C[i], end=' ')
