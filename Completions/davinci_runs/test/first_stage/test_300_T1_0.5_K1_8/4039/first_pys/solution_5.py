

def main():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[1])
    projects.reverse()
    for project in projects:
        if r < project[0]:
            print("NO")
            return
        r += project[1]
        if r < 0:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()