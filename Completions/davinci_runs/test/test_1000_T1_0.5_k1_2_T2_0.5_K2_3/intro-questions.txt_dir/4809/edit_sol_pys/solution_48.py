
def coconut(s, n):
    players = list(range(1, n+1))
    player = 0
    while len(players) > 1:
        player += s - 1
        player %= len(players)  # player = player % len(players)
        players.pop(player)
    return players[0]


print(coconut(int(input()), int(input())))  # n is the number of players and s is the number of coconuts to start with
