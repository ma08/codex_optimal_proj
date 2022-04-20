

def main():
    n, r = map(int, input().split())  # type: int, int
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))  # type: list
    projects.sort(key=lambda x: x[1])
    for project in projects:
        if r >= project[0]:
            r += project[1]
            if r < 0:
                print("NO")
                return
    print("YES")

if __name__ == '__main__':
    main()
