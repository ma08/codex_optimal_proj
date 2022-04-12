

def find_max_team_size(skills):
    unique_skills = set(skills) # set of unique skills
    same_skills = {}
    for skill in skills: # count the number of times each skill appears
        if skill in same_skills:
            same_skills[skill] += 1
        else:
            same_skills[skill] = 1
    
    if len(unique_skills) == 1: # if there is only one skill, no one can be paired
        return 0
    elif len(unique_skills) == 2: # if there are two skills, the minimum number of times that skill appears is the maximum team size
        return min(same_skills.values())
    else: # if there are more than two skills, the minimum number of times that skill appears is the maximum team size
        return min(same_skills.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skills = list(map(int, input().split()))
        print(find_max_team_size(skills))
