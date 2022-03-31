

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

players = [K] * N
for a in A:
    for i in range(N):
        if i != a - 1:
            players[i] -= 1

for player in players:
    if player > 0:
        print("Yes")
    else:
        print("No")