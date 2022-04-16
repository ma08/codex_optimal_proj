

def coconut_splat(s, n):  # s = steps, n = players
    players = [True for _ in range(n)]  # initialize players
    player = 0  # first player
    while True:  # loop
        if players[player] == True:  # if player is still in game
            if s == 1:  # if steps is 1, player is eliminated
                players[player] = False  # eliminate player
            elif s == 2:  # if steps is 2, player is eliminated
                players[player] = False  # eliminate player
            elif s == 3:  # if steps is 3, player is eliminated
                players[player] = False  # eliminate player
            elif s == 4:  # if steps is 4, player is eliminated
                players[player] = False  # eliminate player
            elif s == 5:  # if steps is 5, player is eliminated
                players[player] = False  # eliminate player
            elif s == 6:  # if steps is 6, player is eliminated
                players[player] = False  # eliminate player
            elif s == 7:  # if steps is 7, player is eliminated
                players[player] = False  # eliminate player
            elif s == 8:  # if steps is 8, player is eliminated
                players[player] = False  # eliminate player
            elif s == 9:  # if steps is 9, player is eliminated
                players[player] = False  # eliminate player
            elif s == 10:  # if steps is 10, player is eliminated
                players[player] = False  # eliminate player
        if players.count(True) == 1:  # if only one player is left
            break  # break loop
        player = (player + 1) % n  # next player
    return players.index(True) + 1  # return player index

print(coconut_splat(10, 10))  # print result
