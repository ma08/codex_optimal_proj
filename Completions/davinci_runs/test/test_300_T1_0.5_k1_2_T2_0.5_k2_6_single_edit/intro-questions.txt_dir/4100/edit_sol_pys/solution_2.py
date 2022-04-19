

N, K, Q = [int(i) for i in input().split()]
# initialize players

players = [K] * N
# each time a player win, give him one point
# each time a player lose, take away one point

for i in range(Q):
    A = int(input()) - 1
    players[A] += 1
    for j in range(N):
        if j != A:
            players[j] -= 1
# if a player has more than 0 points, print 'Yes'
# if a player has less than 0 points, print 'No'

for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
