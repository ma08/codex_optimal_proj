


def main():
    n, m = [int(x) for x in input().split()]
    a = [[int(x) for x in input().split()] for _ in range(n + 1)]

    k = 0
    for i in range(n):
        for j in range(n):
            for c in range(m):
                k = max(k, abs(a[j][c] - a[j + 1][c]) + abs(a[j][c] - a[j][c + 1]))

    print(k)


if __name__ == "__main__":
    main()
