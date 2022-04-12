

def main():
    n = int(input())
    skill = [int(x) for x in input().split()]
    skill.sort()
    max_team = 0
    for i in range(n - 1):
        if skill[i + 1] - skill[i] <= 5:
            max_team += 1
    print(max_team+1)


if __name__ == '__main__':
    main()
