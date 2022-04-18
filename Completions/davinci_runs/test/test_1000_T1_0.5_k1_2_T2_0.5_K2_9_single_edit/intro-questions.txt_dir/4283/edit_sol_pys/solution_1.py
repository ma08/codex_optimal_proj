

def main():
    n = int(input())
    skills = [int(x) for x in input().split()]
    skills.sort()
    max_team = 0
    for i in range(n - 1):
        if skills[i + 1] - skills[i] <= 5:
            max_team += 1
    print(max_team+1)


if __name__ == '__main__':
    main()
