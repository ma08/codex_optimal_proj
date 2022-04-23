
N = 100
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append((a, b))

dp = [[0 for i in range(N + 1)] for j in range(m + 1)]
for k in range(1, m + 1):
    for i in range(1, N + 1):
        if stores[k - 1][0] < i:
            dp[k][i] = max(dp[k - 1][i], stores[k - 1][1] + dp[k - 1][i - stores[k - 1][0]])
        else:
            dp[k][i] = dp[k - 1][i]
#-----Solve-----

print(dp[m][N])
#-----Display-----
