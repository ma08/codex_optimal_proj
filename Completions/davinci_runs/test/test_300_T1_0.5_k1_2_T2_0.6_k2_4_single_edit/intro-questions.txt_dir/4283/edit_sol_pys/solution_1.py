

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        skills = [int(x) for x in input().split()]
        skills.sort()
        max_team = 0
        for j in range(n-1):
            if skills[j+1] - skills[j] <= 5:
                max_team += 1
        print(max_team+1)


if __name__ == '__main__':
    main()
