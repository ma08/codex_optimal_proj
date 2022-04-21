
N, K, Q = [int(i) for i in input().split()]

players = [K for i in range(N)]

for i in range(Q):
    A = int(input()) - 1
    players[A] = players[A] + 1
    for j in range(N):
        if j != A:
            players[j] = players[j] - 1

for i in range(N):
    if players[i] > Q:
        print('Yes')
    else:
        print('No')
