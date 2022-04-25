

def main():
    n, k = [int(x) for x in input().split()]
    skills = [int(x) for x in input().split()]
    skills.sort(reverse=True)
    max_team = 0
    for i in range(0, k):
        max_team += skills[i]
    print(max_team)


if __name__ == '__main__':
    main()
