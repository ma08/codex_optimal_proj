
inf = 1000000000000
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])
dp = [[inf for j in range(m+1)] for i in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m+1):
        if j >= stores[i][0]:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-stores[i][0]] + stores[i][1])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[n][m])
#-----Solve-----

#-----Display-----
