

def find_max_team_size(skills):
    unique_skills = list(set(skills))
    same_skills = {}
    for skill in skills:
        if skill in same_skills:
            same_skills[skill] += 1
        else:
            same_skills[skill] = 1
    
    if len(unique_skills) == 1:
        return 0
    elif len(unique_skills) == 2:
        return min(same_skills[unique_skills[0]], same_skills[unique_skills[1]], same_skills[unique_skills[2]])
    else:
        return min(same_skills.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skills = list(map(int, input().split()))
        print(find_max_team_size(skills))
