

def coconut_splat(n, s):
    players = [True for _ in range(n)]
    player_count = n
    splat_count = s
    player = 0
    while True:
        if players[player] == True and splat_count > 1:
            splat_count -= 1
        elif players[player] == True and splat_count == 1:
            players[player] = False
            splat_count = s
        if players.count(True) == 1 and player_count > 1:
            break
        elif players.count(True) == 1 and player_count == 1:
            return 1
        player = (player + 1) % n
    return players.index(True) + 1

print(coconut_splat(10, 2))
