

def CoconutSplat(s, n):
    players = [1] * n
    while len(players) > 1:
        for i in range(s):
            players[0] = (players[0] + 1) % len(players)
            if players[players[0]] == 0:
                players[0] = (players[0] + 1) % len(players)
        players.pop(players[0])
    return players[0] + 1

s, n = map(int, input().split())
print(CoconutSplat(s, n))
