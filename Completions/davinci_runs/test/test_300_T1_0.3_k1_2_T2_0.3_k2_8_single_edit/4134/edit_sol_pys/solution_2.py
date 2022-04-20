
def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    dp[0][0][a[0][0]] = 1
    for i in range(n):  # i行目
        for j in range(m):  # j列目
            for l in range(k + 1):  # l個目
                if i + 1 < n:
                    dp[i + 1][j][l] += dp[i][j][l]
                if j + 1 < m:
                    dp[i][j + 1][l] += dp[i][j][l]
                if i + 1 < n and j + 1 < m:
                    dp[i + 1][j + 1][l ^ a[i + 1][j + 1]] += dp[i][j][l]
    print(dp[n - 1][m - 1][k])


if __name__ == '__main__':
    main()
