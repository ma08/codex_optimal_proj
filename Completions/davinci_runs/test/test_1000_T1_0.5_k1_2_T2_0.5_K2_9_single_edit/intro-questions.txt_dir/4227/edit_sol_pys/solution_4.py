
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)


# DP[i][j] = i番目までの頂点を使って、jを含む場合のパターン数(jはビット表現)
dp = [[0] * (2 ** n) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(2 ** n):
        if dp[i][j] == 0: continue
        for k in edges[i]:
            if j & (1 << k) != 0: continue
            dp[i + 1][j | (1 << k)] += dp[i][j]
print(dp[n][2 ** n - 1])
