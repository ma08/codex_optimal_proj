

def coconut(num_players, num_coconuts):
    players = [1 for x in range(num_players)]
    curr = 0
    for i in range(num_coconuts):
        curr = (curr + 1) % num_players
        if players[curr] == 0:
            while players[curr] == 0:
                curr = (curr + 1) % num_players
        if players[curr] == 1:
            players[curr] = 2
        elif players[curr] == 2:
            players[curr] = 0
    while players[curr] == 0:
        curr = (curr + 1) % num_players
    return curr + 1

def main():
    num_coconuts, num_players = [int(x) for x in input().split()]
    print(coconut(num_players, num_coconuts))

if __name__ == "__main__":
    main()
