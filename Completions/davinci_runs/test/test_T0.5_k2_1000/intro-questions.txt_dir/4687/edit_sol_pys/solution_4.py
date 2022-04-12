# -*- coding: utf-8 -*-

N, K = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

for i in range(N):
    if K <= B[i]:
        print(A[i])
        break
    K -= B[i]
