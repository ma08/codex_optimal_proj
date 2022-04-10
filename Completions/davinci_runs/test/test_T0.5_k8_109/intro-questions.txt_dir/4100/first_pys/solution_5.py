

n, k, q = map(int, input().split())
players = [k] * n
for _ in range(q):
    players[int(input()) - 1] -= 1
for player in players:
    if player > 0:
        print('Yes')
    else:
        print('No')