

N, M = map(int, input().split())
a = list(map(int, [input() for _ in range(M)]))

# 0-originにする
a = [i-1 for i in a]

dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    if i in a:
        dp[i] = 0
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])