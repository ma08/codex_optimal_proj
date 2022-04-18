

def coconut_splat(s, n, k):
    players = [True for _ in range(n)]
    player = 0
    while True:
        if players[player]:
            players[player] = False 
        if players.count(True) == 1: 
            break
        player = (player + 1) % n
    return players.index(True) + 1

print(coconut_splat(10, 10, 1))
