

def coconut(s, n):  # s = step, n = number of players
    players = list(range(1, n + 1))  # create range of players
    player = 0
    while len(players) > 1:  # loop until only 1 player remains
        player += s - 1  # step ahead
        player %= len(players)  # if player exceeds the number of players, go back to the start of the list
        players.pop(player)  # remove player
    return players[0]  # return last player

print(coconut(int(input()), int(input())))
