


def coconut(s, n):  # n is the number of players and s is the number of coconuts to start with
    players = list(range(1, n + 1))
    player = 0
    while len(players) > 1:
        player += s - 1
        player %= len(players)
        players.pop(player)
    return players[0]


if __name__ == '__main__':
    print(coconut(int(input()), int(input())))
