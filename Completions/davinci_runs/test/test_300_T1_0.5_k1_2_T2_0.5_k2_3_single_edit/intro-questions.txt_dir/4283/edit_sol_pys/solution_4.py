

def main():
    n = int(input())
    skills = [int(x) for x in input().split()]
    skills.sort()
    max_team = 0
    i = 0
    while i < n:
        max_team += 1
        j = i
        while j < n and skills[j] - skills[i] <= 5:
            j += 1
        i = j
    print(max_team)


if __name__ == '__main__':
    main()
