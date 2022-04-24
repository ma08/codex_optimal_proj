

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

# a.sort()

skills = defaultdict(list)
for i in range(n):
    skills[a[i]].append(i)

def get_teams(skills, k):
    teams = []
    for skill in sorted(skills):
        while len(skills[skill]) >= 2:
            teams.append((skills[skill].pop(0), skills[skill].pop()))
    for skill in sorted(skills):
        if skills[skill]:
            teams.append((skills[skill].pop(),))
    if len(teams) > k:
        return []
    return teams

teams = get_teams(skills, k)

if not teams:
    print(0)
    exit(0)

for i in range(n-1, -1, -1):
    if a[i] - a[0] <= 5:
        skills[a[i]].append(teams[0][0])
        del teams[0]
        teams = get_teams(skills, k)
        if teams and len(teams) <= k:
            break

if teams:
    print(sum(map(len, teams)))
else:
    print(0)
