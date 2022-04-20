

N, K, Q = [int(i) for i in input().split()]

players = [K] * N

for i in range(Q):
    A = int(input()) - 1
    players[A] += 1 #add 1 to the player
    for j in range(N):
        if j != A: #subtract 1 from the other players
            players[j] -= 1

for i in range(N):
    if players[i] > 0: #check if the player has a positive score
        print('Yes')
    else:
        print('No')
