
import sys
input = sys.stdin.readline()

n, m = map(int, input().split())
edges = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())[:2]
    edges[a - 1] += 1
    edges[b - 1] += 1

# DP[i][j] = i番目までの頂点を使って、jを含む場合のパターン数
dp = [[0] * (2 ** (n + 1)) for _ in range(n + 1)]
dp[0][1 << 1] = 1
for i in range(n):
    for j in range(2 ** (n + 1)):
        if dp[i][j] == 0:
            continue
        for k in range(1, n + 2):
            if j & (1 << k) != 0 or edges[k - 1] == 0:
                continue
            dp[i + 1][j | (1 << k)] += dp[i][j]
print(dp[n][2 ** (n + 1) - 1])
