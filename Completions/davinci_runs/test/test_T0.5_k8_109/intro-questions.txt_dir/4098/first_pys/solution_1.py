

import itertools

def max_students_in_k_teams(skills, k):
    if k == 1:
        return 1

    skills.sort()
    n = len(skills)

    # Generate the indices of all possible teams
    team_idx = list(itertools.combinations(range(n), k))

    # Compute the number of students in each team
    team_size = []
    for i in range(len(team_idx)):
        team_size.append(len(team_idx[i]))

    # Compute the maximum skill and minimum skill of each team
    max_skills = []
    min_skills = []
    for i in range(len(team_idx)):
        max_skills.append(max(skills[j] for j in team_idx[i]))
        min_skills.append(min(skills[j] for j in team_idx[i]))

    # Compute the difference between the maximum skill and minimum skill of each team
    diff = []
    for i in range(len(team_idx)):
        diff.append(max_skills[i] - min_skills[i])

    # Find all teams with difference of 5 or less
    max_students = 0
    for i in range(len(team_idx)):
        if diff[i] <= 5:
            max_students = max(max_students, team_size[i])

    return max_students


if __name__ == "__main__":
    n, k = [int(s) for s in input().split()]
    skills = [int(s) for s in input().split()]
    max_students = max_students_in_k_teams(skills, k)
    print(max_students)