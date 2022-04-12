def main():
    n, a, b, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + (h[i] - 1) // a
            else:
                dp[i][j] = dp[i - 1][j] + (h[i] - 1) // a + (h[i] - 1) // b
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (h[i] - b) // a)
    print(dp[n - 1][k])


if __name__ == '__main__':
    main()
