


def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(tuple(map(int, input().split())))
    projects.sort(key=lambda x: x[1])
    for i in range(n):
        r -= projects[i][0]
        if r < 0:
            print("NO")
            return
        r += projects[i][1]
    print("YES")


if __name__ == "__main__":
    main()