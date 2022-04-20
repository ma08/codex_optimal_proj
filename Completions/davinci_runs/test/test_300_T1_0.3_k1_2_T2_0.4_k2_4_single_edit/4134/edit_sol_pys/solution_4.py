

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            dp[i][j+1] += dp[i][j]
            dp[i+1][j] += dp[i][j]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] -= dp[i][j]
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] ^ k == 0:
                ans += dp[i][j]
    print(ans)

if __name__ == "__main__":
    main()
