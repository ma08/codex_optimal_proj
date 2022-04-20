
INF = float('inf')
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])
dp = [INF] * (n+1)
dp[0] = 0
for i in range(n):
    for j in range(i+1, n+1):
        dp[j] = min(dp[j], dp[i] + abs(stores[i][0] - stores[j][0]) + abs(stores[i][1] - stores[j][1]))
#-----Solve-----

print(dp[n])
#-----Display-----
