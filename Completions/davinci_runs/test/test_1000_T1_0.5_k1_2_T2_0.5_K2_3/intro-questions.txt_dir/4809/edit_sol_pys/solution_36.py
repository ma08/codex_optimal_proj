

def coconut_splat(n, k):
    players = [True for _ in range(n)]
    player = 0
    while True:
        if players[player] == True:
            players[player] = False
        if players.count(True) == 1:
            break
        player = (player + 1) % n
    return players.index(True) + 1

print(coconut_splat(10, 1))
