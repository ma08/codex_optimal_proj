

    import sys
    sys.setrecursionlimit(10**7)
    INF = 10**12
    MOD = 10**9+7

    def rec(n, x):
        if n == 0:
            return 1
        if dp[n][x] != -1:
            return dp[n][x]
        dp[n][x] = 0
        for i in range(1, x+1):
            dp[n][x] += rec(n-1, i)
        return dp[n][x]

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    abcd.sort(key=lambda x: (x[1], x[0]))
    dp = [[0 for _ in range(m)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:
        for j in range(c, m):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[n]))

if __name__ == '__main__':
    main()
