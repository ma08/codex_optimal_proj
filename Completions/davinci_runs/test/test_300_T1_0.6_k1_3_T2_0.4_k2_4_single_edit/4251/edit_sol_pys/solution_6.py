
def main():
    n, m = (int(x) for x in input().split())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    k = -1
    for i in range(n):
        for j in range(i + 1, n):
            for c in range(m):
                k = max(k, abs(a[i][c] - a[j][c]))

    print(k)


if __name__ == "__main__":
    main()
