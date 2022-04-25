
N, K, Q = [int(i) for i in input().split()]  # N: Number of players, K: Initial number of points, Q: Number of queries

players = [K] * N  # Initialize all players with K points

for i in range(Q):  # Execute Q queries
    A = int(input()) - 1
    players[A] += 1  # Add one point to player A
    for j in range(N):
        if j != A:
            players[j] -= 1  # Subtract one point from all other players

for i in range(N):  # Print result
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
