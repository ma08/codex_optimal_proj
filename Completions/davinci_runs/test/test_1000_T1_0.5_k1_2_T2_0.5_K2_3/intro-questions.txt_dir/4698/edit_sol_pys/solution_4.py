# coding: utf-8

# Get inputs
N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX_list = [list(map(int, input().split())) for _ in range(M)]

# Solve
for i in range(M):
    P, X = PX_list[i]
    T[P-1] = X
    print(sum(T))
