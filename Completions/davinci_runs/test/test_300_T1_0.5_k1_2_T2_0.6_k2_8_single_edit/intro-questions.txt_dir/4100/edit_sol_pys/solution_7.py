#!/usr/bin/env python3

N, K, Q = [int(i) for i in input().split()]

players = [K] * N

for i in range(Q):
    A = int(input())
    players[A-1] += 1
    for j in range(N):
        if j != A-1:
            players[j] -= 1

for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
