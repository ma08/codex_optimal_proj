

def coconut_splat(s, n, m):
    players = [i for i in range(1, n+1)]
    while len(players) > 1:
        for i in range(s):
            players[0] = (players[0] + m-1) % len(players)
        players.pop(players[0])
    return players[0] + 1

s, n = map(int, input().split())
print(coconut_splat(s, n))
