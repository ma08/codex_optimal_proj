

def coconut_splat(s, n):
    players = [True for _ in range(n)]
    player = 0
    while players.count(True) > 1:
        if players[player] == True: # if player is still in the game
            if s == 1: # if s is 1
                players[player] = False # player is out of the game
            elif s == 2: # if s is 2
                players[player] = False # player is out of the game
            elif s == 3: # if s is 3
                players[player] = False # player is out of the game
            elif s == 4: # if s is 4
                players[player] = False # player is out of the game
            elif s == 5: # if s is 5
                players[player] = False # player is out of the game
            elif s == 6: # if s is 6
                players[player] = False # player is out of the game
            elif s == 7: # if s is 7
                players[player] = False # player is out of the game
            elif s == 8: # if s is 8
                players[player] = False # player is out of the game
            elif s == 9: # if s is 9
                players[player] = False # player is out of the game
            elif s == 10: # if s is 10
                players[player] = False # player is out of the game
        player = (player + 1) % n # go to the next player
    return players.index(True) + 1 # return the index of the player + 1

print(coconut_splat(10, 10)) # print the result
