

def find_max_team_size(skill_set):
    uniq_skill_set = set(skill_set)
    same_skill_set = {}
    for skill in skill_set:
        same_skill_set[skill] = same_skill_set.get(skill, 0) + 1

    if len(uniq_skill_set) == 1:
        return 0
    elif len(uniq_skill_set) == 2:
        return min(same_skill_set.values())
    else:
        return min(same_skill_set.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skill_set = list(map(int, input().split()))
        print(find_max_team_size(skill_set))
