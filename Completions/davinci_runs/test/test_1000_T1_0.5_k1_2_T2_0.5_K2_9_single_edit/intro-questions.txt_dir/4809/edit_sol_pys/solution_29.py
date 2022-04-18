def CoconutSplat(s, n):
    players = list(range(1, n + 1))
    while len(players) > 1:
        for i in range(s):
            players[0] = (players[0] - 1) % n
            if players[players[0]] == 0:
                players[0] = (players[0] - 1) % n
        players.pop(players[0])
    return players[0] + 1

s, n = map(int, input().split())
print(CoconutSplat(s, n))
