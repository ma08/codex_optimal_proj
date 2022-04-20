
N = int(input())
W = list(map(int, input().split()))

# dp[i][j] = i番目までの荷物を使って、重さの差がj以内になるように分けたときの、重さの和の最大値(jは負の値も含む)
dp = [[0] * (sum(W) + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(sum(W) + 1):
        if j < W[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i - 1]] + W[i - 1])

ans = sum(W)
for j in range(sum(W) + 1):
    ans = min(ans, abs(2 * dp[N][j] - sum(W)))

print(ans)
