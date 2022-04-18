
N, K, Q = [int(i) for i in input().split()]

players = [K - Q] * N

for i in range(Q):
    A = int(input()) - 1
    players[A] += 1 

for i in range(N):
    print('Yes' if players[i] > 0 else 'No')
