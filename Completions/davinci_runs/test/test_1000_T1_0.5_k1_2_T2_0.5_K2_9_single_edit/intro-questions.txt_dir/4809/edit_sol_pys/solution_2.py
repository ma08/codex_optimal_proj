


def coconutSplat(s, n):
    players = list(range(1, n + 1))
    while len(players) != 1:
        for i in range(s - 1):
            players.append(players.pop(0))
        players.pop(0)
    return players[0]


s, n = map(int, input().split(' '))
print(coconutSplat(s, n))
