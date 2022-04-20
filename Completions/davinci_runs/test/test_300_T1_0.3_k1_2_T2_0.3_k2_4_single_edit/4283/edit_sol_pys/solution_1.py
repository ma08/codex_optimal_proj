

def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        skills = list(map(int, input().split()))
        skills.sort()
        max_team_size = 1
        for i in range(n - 1):
            if skills[i + 1] - skills[i] <= 5:
                max_team_size += 1
        print(max_team_size)

if __name__ == '__main__':
    main()
