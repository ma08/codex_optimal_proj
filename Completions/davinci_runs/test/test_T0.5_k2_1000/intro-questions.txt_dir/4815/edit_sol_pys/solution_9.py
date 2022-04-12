


def main():
    """
    Main function that runs the program.
    """
    # Get inputs
    n, p, m = map(int, input().split())  # n: number of players, p: points to win, m: number of games
    players = {}
    for i in range(n):
        players[input()] = 0  # input() is the name of the player
    for i in range(m):
        player, points = input().split()  # input() is the name of the player and points earned
        players[player] += int(points)  # add points to the player's score

    # Check if there are any winners
    winners = []
    for player in players:
        if players[player] >= p:
            winners.append(player)
    if len(winners) > 0:
        for winner in winners:
            print(winner, "wins!")
    else:
        print("No winner!")


if __name__ == "__main__":
    main()
