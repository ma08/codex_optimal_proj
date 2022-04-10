

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0]*(h+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(h+1):
        dp[i][j] = dp[i-1][j]
        if j >= a[i-1]:
            dp[i][j] += dp[i-1][j-a[i-1]]
        if j >= a[i-1]+1:
            dp[i][j] += dp[i-1][j-a[i-1]-1]

ans = 0
for i in range(l, r+1):
    ans += dp[n][i]

print(ans)