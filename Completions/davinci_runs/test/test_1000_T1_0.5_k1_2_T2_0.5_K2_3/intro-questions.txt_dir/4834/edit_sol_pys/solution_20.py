N = int(input())
teams = list(map(int, input().split()))

teams.sort()

print(sum(teams[::2]) + sum(teams[1::2]))
