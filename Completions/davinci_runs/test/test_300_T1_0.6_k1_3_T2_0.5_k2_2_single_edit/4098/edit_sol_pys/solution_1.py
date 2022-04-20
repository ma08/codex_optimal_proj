

from sys import stdin, stdout
from collections import defaultdict

n,k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
# n,k = 5,2
# a = [1, 2, 15, 15, 15]

# n,k = 6,1
# a = [36, 4, 1, 25, 9, 16]

# n,k = 4,4
# a = [1, 10, 100, 1000]

a.sort(key=lambda x: x[1])

skills = defaultdict(int)
for i in range(n):
    skills[a[i]] += 1

def get_skill(skills):
    for skill in skills:
        if skills[skill] > 0:
            return skill

def get_team(skills):
    skill = get_skill(skills)
    if not skill:
        return []
    skills[skill] -= 1
    if skills[skill] == 0:
        del skills[skill]
    team = [skill]
    for skill in skills:
        if skill - team[0] <= 5:
            team.append(skill)
            skills[skill] -= 1
            if skills[skill] == 0:
                del skills[skill]
    return team

def get_teams(skills, k):
    teams = []
    while get_skill(skills):
        teams.append(get_team(skills))
    if len(teams) > k:
        return []
    return teams

teams = get_teams(skills, k)

for i in range(n-1, -1, -1):
    if a[i] - a[0] <= 5:
        skills[a[i]].append(skills[a[0]].pop(0))
        if not skills[a[0]]:
            del skills[a[0]]
        teams = get_teams(skills, k)
        if teams:
            break

stdout.write(str(sum(map(len, teams))) + '\n')
stdout.flush()
