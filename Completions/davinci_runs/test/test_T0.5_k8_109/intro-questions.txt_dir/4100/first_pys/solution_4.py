

#%%
N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

players = [K]*N
for a in A:
    players[a-1] += 1
    for i in range(N):
        if i != a-1:
            players[i] -= 1

for p in players:
    if p > 0:
        print('Yes')
    else:
        print('No')