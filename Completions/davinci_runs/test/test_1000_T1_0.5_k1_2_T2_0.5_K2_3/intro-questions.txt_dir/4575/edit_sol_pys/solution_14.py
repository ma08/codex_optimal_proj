# coding: utf-8

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(D):
        if (j + 1) % A[i] == 0:
            X += 1
    if D % A[i] == 0:
        X += 1

print(X)
