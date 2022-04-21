

A = []
B = []
C = []
from functools import partial

N, M = map(int, input().split())
for i in range(M):
    tmp = list(map(int, input().split()))
    A.append(tmp[0])
    B.append(tmp[1])

A = []
for i in range(K):
    d = int(input())
    A.append(list(map(int, input().split())))

A_flat = []
for i in range(K):
    A_flat.extend(A[i])
A_flat = set(A_flat)

ans = N - len(A_flat)
print(ans)
