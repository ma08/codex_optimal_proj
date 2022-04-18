

def coconut(s, n):
    players = list(range(1, n + 1))
    player = -1
    while len(players) > 1:
        for i in range(s):
            player += 1
            player %= len(players)
        players.pop(player % len(players))
    return players[0]

print(coconut(int(input()), int(input())))
