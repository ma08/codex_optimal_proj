

def dfs(i, j, n, m, d, s):
    if i < 0 or j < 0 or i >= n or j >= m or d[i][j] != 0:
        return
    d[i][j] = s
    dfs(i + 1, j, n, m, d, s)
    dfs(i - 1, j, n, m, d, s)
    dfs(i, j + 1, n, m, d, s)
    dfs(i, j - 1, n, m, d, s)

def main():
    n, m = map(int, input().split())
    d = [[0]*m for i in range(n)]
    s = 1

    for i in range(n):
        l = list(map(int, input().split()))
        for j in range(m):
            if l[j] == 1:
                d[i][j] = -1

    for i in range(n):
        for j in range(m):
            if d[i][j] == 0:
                dfs(i, j, n, m, d, s)
                s += 1

    print(s - 2)

if __name__ == '__main__':
    main()
