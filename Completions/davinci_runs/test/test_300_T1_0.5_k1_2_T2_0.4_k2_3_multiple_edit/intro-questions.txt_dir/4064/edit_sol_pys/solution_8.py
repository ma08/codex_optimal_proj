
import sys

n,h,l,r = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
dp = [[0] * h for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(h):
        dp[i][j] = max(dp[i-1][j],dp[i-1][(j+a[i-1])%h]) #오늘을 잤을 때 안잤을 때 중 큰 값

        if l<=(j+a[i-1])%h<=r:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+1) #만약 오늘을 잤을 때 잠이 좋은 경우

print(max(dp[n]))
