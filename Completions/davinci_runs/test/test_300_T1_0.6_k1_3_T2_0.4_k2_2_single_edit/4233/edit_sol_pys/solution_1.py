
def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input())

    ans = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if a[i][j] == '.':
                continue
            if a[i][j - 1] == '.' and a[i][j + 1] == '.' and a[i - 1][j] == '.' and a[i + 1][j] == '.':
                continue
            s = 1
            while True:
                if i - s < 0 or j - s < 0 or i + s >= n or j + s >= m:
                    break
                if a[i - s][j] == '.' or a[i + s][j] == '.' or a[i][j - s] == '.' or a[i][j + s] == '.':
                    break
                ans.append((i, j, s))
                s += 1
    if len(ans) == 0:
        print(-1)
        return
    print(len(ans))
    for x, y, s in ans:
        print(x + 1, y + 1, s)


if __name__ == "__main__":
    main()
