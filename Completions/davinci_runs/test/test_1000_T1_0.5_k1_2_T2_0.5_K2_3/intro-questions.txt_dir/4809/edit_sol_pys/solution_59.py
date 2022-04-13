

def coconut_splat(s, n):
    players = [True for _ in range(n)]
    player = 0
    while players.count(True) > 1:
        if s == 1:
            players[player] = False
        elif s == 2:
            players[player] = False
        elif s == 3:
            players[player] = False
        elif s == 4:
            players[player] = False
        elif s == 5:
            players[player] = False
        elif s == 6:
            players[player] = False
        elif s == 7:
            players[player] = False
        elif s == 8:
            players[player] = False
        elif s == 9:
            players[player] = False
        elif s == 10:
            players[player] = False
        player = (player + 1) % n
    return players.index(True) + 1

print(coconut_splat(10, 10))
