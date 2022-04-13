

def coconut_splat(n, s):
    players = [1] * n
    while len(players) > 1:
        for i in range(s):
            players[0] = (players[0]+1) % n
            if players[players[0]] == 0: players[0] = (players[0]+1) % n
        players.pop(players[0])
    return players[0] + 1

n, s = map(int, input().split())
print(coconut_splat(n, s))
