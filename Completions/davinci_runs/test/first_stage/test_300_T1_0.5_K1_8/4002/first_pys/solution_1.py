

n, m, k = [int(x) for x in input().split()]
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])

# dp[i][j] = max sum of choosing j elements from the first i rows
dp = [[0] * (m//2 + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m//2 + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        for k in range(j+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j-k] + sum(a[i-1][k:m-k]))

print(dp[-1][-1])