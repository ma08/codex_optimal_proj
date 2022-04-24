

def main():
    n = int(input())
    skills = [int(x) for x in input().split()]
    skills.sort()
    max_teams = 1
    for i in range(n - 1): # 0 to n-2
        if skills[i + 1] - skills[i] <= 5:
            max_teams += 1
    print(max_teams)


if __name__ == '__main__':
    main()
