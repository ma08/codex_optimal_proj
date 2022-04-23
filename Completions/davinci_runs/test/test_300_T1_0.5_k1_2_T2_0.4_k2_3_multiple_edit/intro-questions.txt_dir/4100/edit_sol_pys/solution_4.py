
N, K, Q = map(int, input().split())

players = [K] * N  # set all players' scores to K

for i in range(Q):
    A = int(input()) - 1  # set the player's score to K + 1
    players[A] += 1
    for j in range(N):
        if j != A:
            players[j] -= 1  # decrease all other players' scores by 1

# print the players' scores
for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
