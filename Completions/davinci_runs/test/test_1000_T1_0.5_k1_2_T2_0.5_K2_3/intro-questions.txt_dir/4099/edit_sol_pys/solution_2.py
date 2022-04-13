#!/usr/bin/env python3
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / N

if avg >= M:
    print(0)
    exit()

if K < M:
    print(-1)
    exit()

print(M*N - sumA)
