N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

players = [K - Q] * N
for a in A:
    players[a - 1] += 1

for player in players:
    if player > 0:
        print("Yes")
    else:
        print("No")
