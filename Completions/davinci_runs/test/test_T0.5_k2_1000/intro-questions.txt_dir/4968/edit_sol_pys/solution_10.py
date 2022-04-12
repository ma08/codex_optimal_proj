

def main():
    """
    The main function
    """
    # Read the input
    num_teams, num_teams_damaged, num_teams_reserves = \
        map(int, input().split())
    teams_damaged = list(map(int, input().split()))
    teams_reserves = list(map(int, input().split()))

    # Sort the lists
    teams_damaged.sort()
    teams_reserves.sort()

    # Check if the team with the reserve is damaged
    for team in teams_reserves:
        if team in teams_damaged:
            teams_damaged.remove(team)

    # Check if the team with the damaged kayak is next to the team with the
    # reserve
    for team in teams_damaged:
        if team + 1 in teams_reserves or team - 1 in teams_reserves:
            teams_damaged.remove(team)

    print(len(teams_damaged))

main()
