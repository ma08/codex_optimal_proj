

def coconutSplat(s, n):
    players = [1] * n
    while len(players) > 1:
        for i in range(s):
            if players[(players[0] + 1) % n] == 0:
                players[0] = (players[0] + 1) % n
        players.pop(players[0])
    return players[0] + 1

s, n = map(int, input().split())
print(coconutSplat(s, n))
