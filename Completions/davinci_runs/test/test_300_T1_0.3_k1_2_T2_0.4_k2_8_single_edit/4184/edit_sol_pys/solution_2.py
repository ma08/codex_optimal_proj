
N = int(input())
W = list(map(int, input().split()))

# dp[i][j] = i番目までの荷物から重さの和がjになるように選んだときの、最小の重さの差
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-W[i]] + W[i])
# dp[i][j] = dp[i-1][j] if j < W[i]
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-W[i]] + W[i]) if j >= W[i]

dp = [[float('inf') for _ in range(sum(W)+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(sum(W)+1):
        if j < W[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-W[i]] + W[i])

ans = float('inf')
for i in range(sum(W)//2+1):
    ans = min(ans, abs(dp[N][i] - (sum(W)-dp[N][i])))
print(ans)
