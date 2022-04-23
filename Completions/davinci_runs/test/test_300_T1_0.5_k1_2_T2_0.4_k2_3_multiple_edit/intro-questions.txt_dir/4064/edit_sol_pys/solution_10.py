
import sys

n,h,l,r = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

dp = [[0] * h for _ in range(n)]

for i in range(n):
    for j in range(h):
        dp[i][j] = max(dp[i-1][j],dp[i-1][(j+a[i])%h])

        if l<=(j+a[i])%h<=r:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+1)

print(max(dp[n]))
