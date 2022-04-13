# coding: utf-8

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(D):
    if i + 1 in A:
        X += 1

print(X)
