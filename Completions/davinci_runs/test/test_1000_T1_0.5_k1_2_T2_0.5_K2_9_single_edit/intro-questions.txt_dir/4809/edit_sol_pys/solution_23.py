

def coconut(s, n)
    players = list(range(1, n + 1))  # creates a list of players
    player = 0  # player that gets eliminated
    while len(players) > 1:  # while there is more than one player
        player += s - 1  # add the number of steps
        player %= len(players)  # modulo to get the player that gets eliminated
        players.pop(player)  # remove the player
    return players[0]  # return the last player

print(coconut(int(input()), int(input())))
