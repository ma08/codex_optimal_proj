
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, k+1):
        dp[0][i] = -1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= a[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]] + a[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][k])

main()
