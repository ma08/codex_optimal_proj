

from sys import stdin

[n, k] = [int(x) for x in stdin.readline().strip().split()]
s = stdin.readline().strip()
costs = [0] + [n - len(s[:i]) for i in range(1, n + 1)]

# dp[i][j] is the minimum cost to get the first i characters and sum to j
dp = [[float('inf')] * (k + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(k + 1):
        # If you don't use the ith character, the cost is the same
        dp[i][j] = dp[i - 1][j]
        # If you use the ith character, the cost is the previous cost plus the cost of the ith character
        if j - costs[i] >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - costs[i]] + costs[i])

if dp[n][k] == float('inf'):
    print('-1')
else:
    print(dp[n][k])