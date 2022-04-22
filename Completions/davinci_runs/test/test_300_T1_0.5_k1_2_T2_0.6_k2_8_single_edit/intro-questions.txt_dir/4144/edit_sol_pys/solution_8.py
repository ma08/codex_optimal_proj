

# ref: https://atcoder.jp/contests/abc128/submissions/9120836
# ---- answer ----

N = int(input())

# dp[i][j] ... i桁目まで見たときに、j=0 のときは 0 が含まれていて、j=1 のときは 9 が含まれている
dp = [[0]*2 for _ in range(N+1)]
dp[0][0] = 1
MOD = 10**9+7

for i in range(1,N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
    dp[i][1] = dp[i-1][0] % MOD

print((dp[N][0] + dp[N][1]) % MOD)
