

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # Each team must have at least one member.
    # The number of teams is the number of students
    # divided by the team size, rounded up.
    # The team size is the number of students divided
    # by the number of teams, rounded down.
    num_teams = (n + k - 1) // k
    team_size = n // k

    # The number of teams that are one size larger
    # than the team size is the remainder of n
    # divided by the team size.
    num_large_teams = n % k

    # The number of teams that are one size smaller
    # than the team size is the number of teams
    # minus the number of large teams.
    num_small_teams = num_teams - num_large_teams

    # The sum of the largest team sizes is the sum
    # of the smallest team sizes plus the number
    # of large teams times 5.
    largest_team_sum = team_size * num_small_teams + num_large_teams * (team_size + 1)

    # The sum of the smallest team sizes is the sum
    # of the smallest team sizes plus the number
    # of large teams times 5.
    smallest_team_sum = team_size * num_small_teams + num_large_teams * (team_size - 1)

    # The largest team size is the team size plus one.
    largest_team_size = team_size + 1

    # The smallest team size is the team size minus one.
    smallest_team_size = team_size - 1

    # The largest team size is the team size plus one.
    largest_team_size = team_size + 1

    # The smallest team size is the team size minus one.
    smallest_team_size = team_size - 1

    # The largest teams are formed by taking the largest
    # team size elements from the start of the sorted array.
    largest_team_sum += sum(a[:largest_team_size * num_large_teams])

    # The smallest teams are formed by taking the smallest
    # team size elements from the end of the sorted array.
    smallest_team_sum += sum(a[-smallest_team_size * num_small_teams:])

    print(largest_team_sum if largest_team_sum >= smallest_team_sum else smallest_team_sum)

if __name__ == '__main__':
    main()