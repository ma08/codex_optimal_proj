
N, K, Q = [int(i) for i in input().split()]
players = [K] * N  # set all players score to K

for i in range(Q):
    A = int(input()) - 1
    players[A] += 1  # increase score of player A
    for p in players:
        if p != A:
            players[p] -= 1  # decrease score of other players

for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
