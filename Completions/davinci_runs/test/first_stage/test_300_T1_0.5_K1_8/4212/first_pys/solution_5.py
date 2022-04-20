

N, M, Q = map(int, input().split())

# dp[i][j] = A_iまでで、A_iがjの時の最大スコア
dp = [[0] * (M+1) for _ in range(N+1)]

for _ in range(Q):
    ai, bi, ci, di = map(int, input().split())
    if ai == 1:
        dp[bi][ci] = max(dp[bi][ci], di)
    else:
        for j in range(ci+1):
            dp[bi][j] = max(dp[bi][j], dp[ai-1][ci-j] + di)

print(max(dp[N]))