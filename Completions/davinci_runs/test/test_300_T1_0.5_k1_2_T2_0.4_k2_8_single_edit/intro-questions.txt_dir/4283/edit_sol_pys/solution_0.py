

def main():
    n = int(input())
    skills = [int(x) for x in input().split()]
    skills.sort()
    print(skills)


if __name__ == '__main__':
    main()
