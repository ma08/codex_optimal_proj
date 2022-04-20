
INF = 10**10
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
    dp[i+1] = min(dp[i+1], dp[i] + stores[i][0])
    dp[i+2] = min(dp[i+2], dp[i] + stores[i][1])
#-----Solve-----

print(dp[-1])
#-----Display-----
