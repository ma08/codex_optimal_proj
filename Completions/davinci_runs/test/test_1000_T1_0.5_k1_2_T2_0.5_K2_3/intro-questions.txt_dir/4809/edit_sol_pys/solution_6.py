

def coconut(s, n):  # s - число кокосов, n - количество игроков
    players = list(range(1, n + 1))
    player = 0
    while len(players) > 1:
        player += s - 1
        player %= len(players)
        players.pop(player)
    return players[0]

print(coconut(int(input()), int(input())))  # ввод числа кокосов и игроков
