

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i + 1 < n:
                dp[i + 1][j] += dp[i][j]
            if j + 1 < m:
                dp[i][j + 1] += dp[i][j]
    dp2[0][0] = a[0][0]
    for i in range(1, n):
        dp2[i][0] = dp2[i - 1][0] ^ a[i][0]
    for i in range(1, m):
        dp2[0][i] = dp2[0][i - 1] ^ a[0][i]
    for i in range(1, n):
        for j in range(1, m):
            dp2[i][j] = dp2[i - 1][j] ^ dp2[i][j - 1] ^ a[i][j]
    ans = 0
    for i in range(n):
        for j in range(m):
            if dp2[i][j] == k:
                ans += dp[i][j]
    print(ans)

if __name__ == '__main__':
    main()
