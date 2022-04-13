

def coconut(s, n):  # n is the number of players and s is the number of coconuts to start with
    players = list(range(n))
    player = 0
    while len(players) > 1:
        player += s
        player %= len(players)
        players.pop(player)
    return players[0]

print(coconut(int(input()), int(input())) + 1)
