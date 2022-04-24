

from sys import stdin
from collections import defaultdict

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
# n,k = 5,2
# a = [1, 2, 15, 15, 15]

# n,k = 6,1
# a = [36, 4, 1, 25, 9, 16]

# n,k = 4,4
# a = [1, 10, 100, 1000]

a.sort(reverse=True)

skills = defaultdict(list)
for i in range(n):
    skills[a[i]].append(i)

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

teams = get_teams(skills, k)

for i in range(n - 1, -1, -1):
    if a[i] - a[-1] <= 5:
        skills[a[i]].append(skills[a[-1]].pop(0))
        if not skills[a[-1]]:
            del skills[a[-1]]
        teams = get_teams(skills, k)
        if teams:
            break

print(sum(map(len, teams)))
