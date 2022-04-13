

n, p, m = [int(x) for x in raw_input().split()]
players = {}

for i in range(n):
    players[raw_input()] = 0

for i in range(m):
    player, points = raw_input().split()
    players[player] += int(points)
    if players[player] >= p:
        print(player + " wins!")
        break
else:
    print("No winner! ")
