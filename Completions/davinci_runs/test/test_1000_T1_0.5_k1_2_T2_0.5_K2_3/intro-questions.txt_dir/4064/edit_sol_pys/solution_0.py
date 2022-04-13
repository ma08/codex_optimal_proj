
import sys

n,h,l,r = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

dp = [[-1] * h for _ in range(n+1)]

dp[0][0] = 0
for i in range(n):
    for j in range(h):        
        if dp[i][j] != -1:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            dp[i+1][(j+a[i])%h] = max(dp[i+1][(j+a[i])%h],dp[i][j])

            if l<=(j+a[i])%h<=r:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j]+1)
                dp[i+1][(j+a[i])%h] = max(dp[i+1][(j+a[i])%h],dp[i][j]+1)

print(max(dp[n]))    
