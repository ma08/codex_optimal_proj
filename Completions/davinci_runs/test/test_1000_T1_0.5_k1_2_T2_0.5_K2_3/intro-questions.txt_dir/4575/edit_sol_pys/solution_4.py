# coding: utf-8

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(D):
    for a in A:
        if (i + 1) % a == 0:
            X += 1 

print(X)
