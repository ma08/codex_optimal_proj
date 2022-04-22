import math


N = int(input())

players = [0] * N
ans = 0

for i in range(N):
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
