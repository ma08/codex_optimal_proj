
def main():
    """
    Main function that runs the program.
    """
    # Get input
    n, p, m = map(int, input().split())
    players = {}
    for i in range(n):
        players[input()] = 0
    for i in range(m):
        player, points = input().split()
        players[player] += int(points)

    # Check if there is any winner
    winners = []
    for player in players:
        if players[player] >= p:
            winners.append(player)
    if len(winners) == 1:
        print(winners[0], "wins!")
    elif len(winners) > 1:
        for winner in winners:
            print(winner)
    else:
        print("No winner!")


if __name__ == "__main__":
    main()
