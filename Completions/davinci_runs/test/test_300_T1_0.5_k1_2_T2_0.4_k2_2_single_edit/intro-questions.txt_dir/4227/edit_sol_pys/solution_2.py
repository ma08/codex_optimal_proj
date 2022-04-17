
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1] += 1
    edges[b - 1] += 1

# DP[i][j] = i番目までの頂点を使って、jを含む場合のパターン数（jは2進数）
dp = [[0] * (1 << n) for _ in range(n)]
dp[0][1 << 0] = 1
for i in range(1, n):
    for j in range(1 << n):
        if j & (1 << i) == 0:
            continue
        for k in range(n):
            if j & (1 << k) == 0 or edges[k] == 0:
                continue
            dp[i][j] += dp[i - 1][j ^ (1 << i)]
print(dp[n - 1][(1 << n) - 1])
