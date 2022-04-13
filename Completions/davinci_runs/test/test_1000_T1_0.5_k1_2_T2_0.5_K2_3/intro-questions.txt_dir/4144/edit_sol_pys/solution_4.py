# https://atcoder.jp/contests/abc149/tasks/abc149_d

# ---- answer ----

k,r = map(int,input().split())
s = input()
n = int(input())

# dp[i][j] ... i 桁目まで見たときに、j=0 のときは 0 が含まれている、j=1 のときは 9 が含まれている、j=2 のときは 0 と 9 が含まれている
dp = [[0]*3 for _ in range(n+1)]
dp[0][2] = 1
mod = 10**9 + 7

for i in range(n):
    if s[i] == '0':
        dp[i+1][0] = (dp[i][0] + dp[i][2]) % mod
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = dp[i][2]
    elif s[i] == '9':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = (dp[i][1] + dp[i][2]) % mod
        dp[i+1][2] = dp[i][2]
    else:
        dp[i+1][0] = (dp[i][0] + dp[i][2]) % mod
        dp[i+1][1] = (dp[i][1] + dp[i][2]) % mod
        dp[i+1][2] = dp[i][2]

ans = (dp[n][0] + dp[n][1] + dp[n][2]) % mod
print(ans)
