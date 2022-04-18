

def coconut_splat(s, n):
    players = list(range(1, n + 1))
    while len(players) > 1:  # for each round
        for i in range(s):  # for each player
            if players[0] == 0:  # player is out of game
                players.pop(0)
            else:
                players.append(players.pop(0))  # pass coconut
        players.pop(0)  # remove player who got the coconut
    return players[0]

s, n = map(int, input().split())
print(CoconutSplat(s, n))
