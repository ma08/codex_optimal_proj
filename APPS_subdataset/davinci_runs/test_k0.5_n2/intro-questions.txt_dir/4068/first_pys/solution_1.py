

n, m = map(int, input().split())
broken = [int(input()) for _ in range(m)]

dp = [0] * (n + 2)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    if i not in broken:
        dp[i] = dp[i - 1] + dp[i - 2]
    elif i - 1 not in broken:
        dp[i] = dp[i - 1]
    elif i - 2 not in broken:
        dp[i] = dp[i - 2]
    else:
        dp[i] = 0

print(dp[n] % (10 ** 9 + 7))