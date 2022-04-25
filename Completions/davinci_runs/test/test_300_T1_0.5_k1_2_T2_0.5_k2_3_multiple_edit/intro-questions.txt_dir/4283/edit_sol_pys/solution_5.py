

def main():
    n = int(input())
    skills = [int(x) for x in input().split()]
    skills.sort()
    max_team = 0
    team = 1
    for i in range(n-1):
        if skills[i+1] - skills[i] <= 5:
            team += 1
        else:
            if team > max_team:
                max_team = team
            team = 1
    if team > max_team:
        max_team = team
    print(max_team)


if __name__ == '__main__':
    main()
