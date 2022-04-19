from collections import deque


N, K, Q = [int(i) for i in input().split()]

players = [K] * N

for i in range(Q):
    A = int(input())
    players[A - 1] += 1

for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
