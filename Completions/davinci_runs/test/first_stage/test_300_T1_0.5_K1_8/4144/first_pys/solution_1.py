

# N = int(input())
N = 10**6

# 問題を分解する
# dp[i][j] := i桁目まで見て、i桁目がjで終わるときの総数
# dp[i][j] = sum(dp[i-1][k]) (j-1<=k<=j+1) (k!=0)
# dp[i][0] = sum(dp[i-1][k]) (k!=0)

# 初期値
dp = [[0]*10 for _ in range(N+1)]
dp[0][0] = 1
dp[0][9] = 1

# 更新
for i in range(1, N+1):
    for j in range(1, 10):
        k = j-1
        if k >= 0:
            dp[i][j] += dp[i-1][k]
        k = j
        dp[i][j] += dp[i-1][k]
        k = j+1
        if k <= 9:
            dp[i][j] += dp[i-1][k]
    # 0桁目は0で終わらない
    dp[i][0] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][6] + dp[i-1][7] + dp[i-1][8] + dp[i-1][9]

# 答え
ans = 0
for j in range(10):
    ans += dp[N][j]
print(ans % (10**9 + 7))