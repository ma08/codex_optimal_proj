

def coconut(s, n):  # s is the number of steps, n is the number of players
    players = list(range(1, n + 1))
    player = 0
    while len(players) > 1:
        player += s - 1
        player %= len(players)
        players.pop(player)

    return players[0]

print(coconut(int(input()), int(input())))
