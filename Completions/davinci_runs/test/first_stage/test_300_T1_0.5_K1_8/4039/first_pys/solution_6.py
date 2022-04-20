


def main():
    n, r = [int(x) for x in input().split()]
    projects = []
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        projects.append((a, b))
    projects.sort(reverse=True)
    for a, b in projects:
        if r < a:
            print("NO")
            return
        r += b
        if r < 0:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()