


def main():
    n, m = (int(x) for x in input().split())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    mx = 0
    for i in range(n):
        for j in range(n - 1):
            for c in range(m):
                mx = max(mx, abs(a[j][c] - a[j + 1][c]))

    print(mx)


if __name__ == "__main__":
    main()
