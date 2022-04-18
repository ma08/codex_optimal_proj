

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split())

dp = [0] * n

for i in range(1,n):
    if a[i-1]<a[i]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = dp[i-1]

for i in range(n-1,0,-1):
    if a[i-1]>a[i]:
        dp[i-1] = max(dp[i-1],dp[i]+1)

print(sum(dp))
