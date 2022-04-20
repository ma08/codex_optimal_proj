
def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0]*(x+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, x+1):
            dp[i][j] = dp[i-1][j]
            if i >= k:
                dp[i][j] = max(dp[i][j], dp[i-k][j-1] + a[i-1])
    print(dp[n][x])

main()
