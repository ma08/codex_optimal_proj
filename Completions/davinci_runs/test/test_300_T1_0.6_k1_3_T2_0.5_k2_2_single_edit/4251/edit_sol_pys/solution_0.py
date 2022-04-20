
def main():
    n, m = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    k = 0
    for i in range(n):
        for j in range(n - 1):
            for c in range(m):
                k = max(k, abs(a[j][c] - a[j + 1][c]))

    print(k)


if __name__ == "__main__":
    main()
