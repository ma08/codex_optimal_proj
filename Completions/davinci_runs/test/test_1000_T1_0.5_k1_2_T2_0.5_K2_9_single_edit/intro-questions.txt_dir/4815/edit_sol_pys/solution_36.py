


def main():
    """
    Main function that runs the program.
    """
    # Get input
    n, p, m = map(int, input().split())  # n = number of players, p = points needed to win, m = number of games
    players = {}
    for i in range(n):
        players[input()] = 0  # player name = points
    for i in range(m):
        player, points = input().split()  # player name = points
        players[player] += int(points)

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
