
def main():
    """
    Main function that runs the program.
    """
    # Get input
    n, p, m = map(int, raw_input().split())
    players = {}
    for i in range(n):
        players[raw_input()] = 0
    for i in range(m):
        player, points = raw_input().split()
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
