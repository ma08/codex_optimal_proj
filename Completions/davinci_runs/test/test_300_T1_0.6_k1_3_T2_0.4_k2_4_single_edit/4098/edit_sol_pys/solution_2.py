

from sys import stdin
from collections import defaultdict

n,k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
# n,k = 5,2
# a = [1, 2, 15, 15, 15]

# n,k = 6,1
# a = [36, 4, 1, 25, 9, 16]

# n,k = 4,4
# a = [1, 10, 100, 1000]

a.sort()

def get_teams(skills, k):
    def get_teams_helper(skills):
        teams = []
        for skill in skills:
            while len(skills[skill]) >= 2:
                teams.append((skills[skill].pop(0), skills[skill].pop()))
        for skill in skills:
            if skills[skill]:
                teams.append((skills[skill].pop(),))
        return teams

    teams = get_teams_helper(skills)
    if len(teams) > k:
        return []
    return teams

for i in range(n-1, -1, -1):
    skills = defaultdict(list)
    for j in range(n):
        skills[a[j]].append(j)
    teams = get_teams(skills, k)
    if teams:
        break

    a[i] += 1

print(sum(map(len, teams)))
