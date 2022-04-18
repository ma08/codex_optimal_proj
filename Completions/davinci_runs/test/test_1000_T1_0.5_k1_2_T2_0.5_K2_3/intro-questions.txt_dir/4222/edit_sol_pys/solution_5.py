# coding: utf-8

N, K = map(int, raw_input().split())

A = []
for i in range(K):
    d = int(raw_input())
    A.append(list(map(int, raw_input().split())))

A_flat = []
for i in range(K):
    A_flat.extend(A[i])
A_flat = set(A_flat)

ans = N - len(A_flat)
print(ans)
