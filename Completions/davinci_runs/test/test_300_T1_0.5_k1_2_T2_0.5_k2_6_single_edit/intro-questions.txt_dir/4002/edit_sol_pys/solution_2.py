import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0 for i in range(k+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= k//2:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1][j-1] + a[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
