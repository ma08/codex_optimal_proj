
print(N, K, Q)
N, K, Q = [int(i) for i in input().split()]

print(players)
players = [K] * N

for i in range(Q):
    print(A)
    A = int(input()) - 1
    print(players)
    players[A] += 1
    for j in range(N):
            print(j)
        if j != A:
            print(players)
            players[j] -= 1

for i in range(N):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
