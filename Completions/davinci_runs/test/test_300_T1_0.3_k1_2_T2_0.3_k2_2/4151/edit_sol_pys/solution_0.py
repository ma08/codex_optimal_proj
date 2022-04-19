

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split())) + [0]
    b = list(map(int, input().split())) + [0]

    # dp[i][j] = number of ways to renumber a[:i] and b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if i < n and j < m and a[i] == b[j]:
                dp[i + 1][j + 1] += dp[i][j]
            if i < n:
                dp[i + 1][j] += dp[i][j]
            if j < m:
                dp[i][j + 1] += dp[i][j]

    print(dp[n][m])


MOD = 998244353

if __name__ == '__main__':
    main()
