
def main():
    """
    Main function that runs the program.
    """
    # Get input
    n, p, m = map(int, input().split())  # n=number of players, p=points needed to win, m=number of games
    players = {}
    for i in range(n):
        players[input()] = 0  # create dictionary entry for each player and set initial points to 0
    for i in range(m):
        player, points = input().split()
        players[player] += int(points)  # add the points from the game to the player's total

    # Check if there are any winners
    winners = []
    for player in players:
        if players[player] >= p:  # check if player has enough points to win
            winners.append(player)
    if len(winners) > 0:  # if there is at least one winner, print their name
        for winner in winners:
            print(winner, "wins!")
    else:  # if no players have enough points to win, print "No winner!"
        print("No winner!")


if __name__ == "__main__":
    main()
