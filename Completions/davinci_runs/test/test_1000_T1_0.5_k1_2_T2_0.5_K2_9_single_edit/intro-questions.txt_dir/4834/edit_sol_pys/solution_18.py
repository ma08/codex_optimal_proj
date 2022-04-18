

N = int(input())  # number of teams
teams = list(map(int, input().split()))  # team members

teams.sort()  # sort teams in ascending order

print(sum(teams[0::2]) + sum(teams[1::2]))
