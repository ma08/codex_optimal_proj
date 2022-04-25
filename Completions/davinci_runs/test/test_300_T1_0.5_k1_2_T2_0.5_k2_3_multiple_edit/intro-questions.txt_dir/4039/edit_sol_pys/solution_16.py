import sys



def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))

    projects.sort(key=lambda x: x[1])

    for project in projects:
        if project[0] > r:
            print("NO")
            sys.exit()
        r += project[1]
        if r < 0:
            print("NO")
            sys.exit()

    print("YES")


if __name__ == '__main__':
    main()
