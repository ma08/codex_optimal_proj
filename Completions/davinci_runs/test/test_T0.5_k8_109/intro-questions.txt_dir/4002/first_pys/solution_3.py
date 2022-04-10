


def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    dp = [[0] * (m // 2 + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(min(m // 2 + 1, m - j + 1)):
            if j == 0:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - 1], dp[i][j - 1] + a[i][j * 2 - 1])
    print(dp[n][m // 2])


if __name__ == '__main__':
    main()