

def main():
    n, m, k = map(int, input().split())
    a = [list(map(lambda x: int(x) % k, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i + 1 < n:
                dp[i + 1][j] += dp[i][j]
            if j + 1 < m:
                dp[i][j + 1] += dp[i][j]
    dp3 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        dp2[i][0] = dp2[i - 1][0] + a[i][0]
        dp3[i][0] = dp3[i - 1][0] + (a[i][0] == 0)
    for j in range(1, m):
        dp2[0][j] = dp2[0][j - 1] + a[0][j]
        dp3[0][j] = dp3[0][j - 1] + (a[0][j] == 0)
    for i in range(1, n):
        for j in range(1, m):
            dp2[i][j] = dp2[i - 1][j] + dp2[i][j - 1] - dp2[i - 1][j - 1] + a[i][j]
            dp3[i][j] = dp3[i - 1][j] + dp3[i][j - 1] - dp3[i - 1][j - 1] + (a[i][j] == 0)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if dp2[i][j] == 0:
                dp[i][j] = 0
            elif dp2[i][j] == k:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1]
    print(dp[0][0])

if __name__ == '__main__':
    main()
