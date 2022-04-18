

n, k, q = [int(i) for i in input().split()]

players = [k] * n

for i in range(Q):
    a = int(input()) - 1
    players[a] += 1
    for j in range(n):
        if j != a:
            players[j] -= 1

for i in range(n):
    if players[i] > 0:
        print('Yes')
    else:
        print('No')
