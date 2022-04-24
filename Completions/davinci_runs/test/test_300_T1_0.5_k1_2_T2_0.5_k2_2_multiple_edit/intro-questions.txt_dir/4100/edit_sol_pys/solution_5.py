# -*- coding: utf-8 -*-


N, M = [int(i) for i in input().split()]
cards = [int(i) for i in input().split()]

ans = 0

for i in range(M):
    A = int(input()) - 1
    players[A] += 1
    for j in range(N):
        if j != A:
            players[j] -= 1

for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
