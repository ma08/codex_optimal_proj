# coding: utf-8

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

# DP[i][j] = i番目までの頂点を使って、jを含む場合のパターン数
dp = [[0] * (1 << n) for _ in range(n)]
dp[0][1 << 0] = 1
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j) == 0:
            continue  # 頂点jが既に使われている場合はスキップ
        for k in edges[j]:
            if i & (1 << k) != 0:  # 頂点kが既に使われている場合はスキップ
                continue
            dp[k][i | (1 << k)] += dp[j][i]
print(dp[0][(1 << n) - 1])
