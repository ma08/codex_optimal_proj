
INF = 10000000000
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())


stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])

#dp[i][j] = min(dp[i][k] + dp[k][j])
dp = [[INF for i in range(n)] for j in range(n)]

for i in range(n):
    dp[i][i] = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            if (stores[i][1] + stores[k][0] <= stores[j][0]):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                dp[j][i] = dp[i][j]

for i in range(n):
    for j in range(n):
        print(dp[i][j], end = " ")
    print()
#-----Solve-----

#-----Display-----
