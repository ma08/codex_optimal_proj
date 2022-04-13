

def find_max_team_size(skill_sets):
    uniq_skill_sets = set(skill_sets)
    same_skill_sets = {}
    for skill in skill_sets:
        same_skill_sets[skill] = same_skill_sets.get(skill, 0) + 1
    
    if len(uniq_skill_sets) == 1:
        return 0
    elif len(uniq_skill_sets) == 2:
        return min(same_skill_sets.values())
    else:
        return min(same_skill_sets.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skill_sets = list(map(int, input().split()))
        print(find_max_team_size(skill_sets))
