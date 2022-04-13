import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j >= m//2 and i >= n//2:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1][j-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][m])
