# coding: utf-8

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in A:
    for j in range((D + 1) // i):
        X += 1

print(X)
