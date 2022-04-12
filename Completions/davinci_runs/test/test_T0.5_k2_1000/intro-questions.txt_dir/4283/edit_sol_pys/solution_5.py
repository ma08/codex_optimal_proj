

def main():
    n = int(input())
    skills_list = [int(x) for x in input().split()]
    skills_list.sort()
    max_team = 0
    for i in range(n - 1):
        if skills_list[i + 1] - skills_list[i] <= 5:
            max_team += 1
    print(max_team+1)


if __name__ == '__main__':
    main()
