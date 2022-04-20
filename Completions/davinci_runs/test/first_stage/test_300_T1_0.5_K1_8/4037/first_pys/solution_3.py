

def main():
    n, r = [int(x) for x in input().split()]
    projects = []
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        projects.append((a, b))
    projects.sort()
    ans = 0
    for project in projects:
        if r >= project[0]:
            r += project[1]
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()