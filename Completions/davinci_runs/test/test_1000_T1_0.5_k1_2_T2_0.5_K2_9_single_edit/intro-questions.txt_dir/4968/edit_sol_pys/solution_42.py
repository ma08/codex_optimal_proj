

def main():
    """
    The main function
    """
    # Read the input
    _, num_teams_damaged, num_teams_reserve = map(int, input().split())
    teams_damaged = list(map(int, input().split()))
    teams_reserve = list(map(int, input().split()))

    # Sort the lists
    teams_damaged.sort()
    teams_reserve.sort()

    # Check if the team with the reserve is damaged,
    # if it is then remove it from the list of damaged teams
    for i in range(len(teams_reserve)):
        if teams_reserve[i] in teams_damaged:
            teams_damaged.remove(teams_reserve[i])

    # Check if the team with the damaged kayak is next to the team with the reserve
    for team in teams_damaged:
        if team + 1 in teams_reserve or team - 1 in teams_reserve:
            teams_damaged.remove(team)

    print(len(teams_damaged))

main()
