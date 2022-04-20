
INF = 10**9
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])

dp = [[INF for _ in range(n+1)] for _ in range(m+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(m+1):
        if i >= 1 and j >= stores[i-1][0]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-stores[i-1][0]] + stores[i-1][1])
        if i >= 1:
            dp[i][j] = min(dp[i][j], dp[i-1][j])

ans = 0
for i in range(m+1):
    if dp[n][i] <= m:
        ans = max(ans, i)

print(ans)
#-----Solve-----

#-----Display-----
