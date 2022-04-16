

def find_max_team_size(skills):
    uniq_skills = set(skills)
    same_skills = {}
    for skill in skills:
        if skill in same_skills:
            same_skills[skill] += 1
        else:
            same_skills[skill] = 1
    
    if len(uniq_skills) == 1:
        return 0
    elif len(uniq_skills) == 2:
        return min(same_skills.values()) - 1
    else:
        return min(same_skills.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skills = list(map(int, input().split()))
        print(find_max_team_size(skills))
