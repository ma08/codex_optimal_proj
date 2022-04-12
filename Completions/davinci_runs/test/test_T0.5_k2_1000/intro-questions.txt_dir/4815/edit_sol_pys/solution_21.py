
def main():
    """
    Main function that runs the program.
    """
    # Get input
    n, p, m = map(int, input().split())  # pylint: disable=invalid-name
    players = {}
    for i in range(n):
        players[input()] = 0  # pylint: disable=invalid-name
    for i in range(m):
        player, points = input().split()  # pylint: disable=invalid-name
        players[player] += int(points)  # pylint: disable=invalid-name

    # Check if there are any winners
    winners = []
    for player in players:  # pylint: disable=invalid-name
        if players[player] >= p:  # pylint: disable=invalid-name
            winners.append(player)  # pylint: disable=invalid-name
    if len(winners) > 0:
        for winner in winners:  # pylint: disable=invalid-name
            print(winner, "wins!")  # pylint: disable=invalid-name
    else:
        print("No winner!")


if __name__ == "__main__":
    main()
