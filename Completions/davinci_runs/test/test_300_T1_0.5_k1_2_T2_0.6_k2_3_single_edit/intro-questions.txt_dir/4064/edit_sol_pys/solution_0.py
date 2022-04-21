import sys
input = sys.stdin.readline


n,h,l,r = map(int,input().split())
a = list(map(int,input().split()))

dp = [[0] * h for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(h):
        dp[i][j] = max(dp[i-1][j],dp[i-1][(j+a[i-1])%h])

        if l<=(j+a[i-1])%h<=r:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+1)

print(max(dp[n]))
