

def coconut(n, s): # n = number of players, s = number of skips
    players = list(range(1, n + 1)) # list of players
    player = 0 # current player
    while len(players) > 1: # loop until there is only one player left
        player += s - 1 # skip to the next player
        player %= len(players) # loop back to the first player
        players.pop(player) # remove the current player
    return players[0] # return the last remaining player

print(coconut(int(input()), int(input())))
