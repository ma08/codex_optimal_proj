

from sys import stdin
from collections import defaultdict

n,k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

a.sort()

def get_teams(skills, k):
    teams = []
    for skill in skills:
        while len(skills[skill]) >= 2:
            teams.append((skills[skill].pop(0), skills[skill].pop()))
    for skill in skills:
        if skills[skill]:
            teams.append((skills[skill].pop(),))
    if len(teams) > k:
        return []
    return teams

skills = defaultdict(list)
for i in range(n):
    skills[a[i]].append(i)

teams = get_teams(skills, k)
for i in range(n-1, -1, -1):
    if a[i] - a[0] <= 5:
        skills[a[i]].append(skills[a[0]].pop(0))
        if not skills[a[0]]:
            del skills[a[0]]
        teams = get_teams(skills, k)
        if teams:
            break

print(sum(map(len, teams)))
