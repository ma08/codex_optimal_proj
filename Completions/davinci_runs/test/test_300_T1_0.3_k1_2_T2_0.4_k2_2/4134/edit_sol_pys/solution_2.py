

    import sys
    sys.setrecursionlimit(10 ** 6)
def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1 % k
    for i in range(n - 1):
        dp[i + 1][0] = dp[i][0]
    for j in range(m - 1):
        dp[0][j + 1] = dp[0][j]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % k
            dp[i][j] = (dp[i][j] * a[i][j]) % k
    print(dp[-1][-1])

if __name__ == '__main__':
    main()
