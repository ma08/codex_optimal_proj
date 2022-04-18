n, p, m = [int(x) for x in input().split()]  # number of players, points, matches
players = {}

for i in range(n):
    players[input()] = 0

for j in range(m):
    player, points = input().split()
    players[player] += int(points)
    if players[player] >= p:
        print(player + " wins!")
        break
else:
    print("No winner!")
