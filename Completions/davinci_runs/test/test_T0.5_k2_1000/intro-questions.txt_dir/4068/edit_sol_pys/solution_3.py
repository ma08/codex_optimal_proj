n, m = map(int, input().split())
broken = set(map(int, input().split()))

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if i in broken:
        continue
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 1000000007)
