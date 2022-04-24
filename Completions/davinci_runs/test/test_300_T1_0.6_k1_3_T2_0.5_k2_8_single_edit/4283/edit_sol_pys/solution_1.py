
def main():
    n = int(input())
    for i in range(n):
        print(i+1)
        

def main():
    n = int(input())
    skills = [int(i) for i in input().split()]
    skills.sort()

    max_team_size = 1
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n and skills[j] - skills[i] <= 5:
            j += 1
        max_team_size = max(max_team_size, j - i)
        i += 1

    print(max_team_size)


if __name__ == '__main__':
    main()
