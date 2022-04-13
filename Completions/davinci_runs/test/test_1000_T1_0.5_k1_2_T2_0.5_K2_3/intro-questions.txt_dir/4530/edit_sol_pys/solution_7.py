

def find_max_team_size(skill):
    unique_skill = set(skill)
    same_skill = {}
    for sk in skill:
        if sk in same_skill:
            same_skill[sk] += 1
        else:
            same_skill[sk] = 1

    if len(unique_skill) == 1:
        return 0
    elif len(unique_skill) == 2:
        return min(same_skill.values())
    else:
        return min(same_skill.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skill = list(map(int, input().split()))
        print(find_max_team_size(skill))
