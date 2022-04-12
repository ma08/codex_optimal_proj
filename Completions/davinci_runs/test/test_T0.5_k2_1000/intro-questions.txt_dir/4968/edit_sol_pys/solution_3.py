

def main():
    """
    The main function
    """
    # Read the input
    num_teams, num_teams_damaged, num_teams_reserve = map(int, input().split())  # pylint: disable=unused-variable
    teams_damaged = list(map(int, input().split()))
    teams_reserve = list(map(int, input().split()))

    # Sort the lists
    teams_damaged.sort()
    teams_reserve.sort()

    # Check if the team with the reserve is damaged
    for team in teams_reserve:
        if team in teams_damaged:
            teams_damaged.remove(team)

    # Check if the team with the damaged kayak is next to the team with the reserve kayak
    for team in teams_damaged:
        if team + 1 in teams_reserve or team - 1 in teams_reserve:
            teams_damaged.remove(team)

    print(len(teams_damaged))

main()
