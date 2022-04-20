

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

if x < k:
    print(-1)
    quit()

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = max(dp[i], dp[i-k+1] + a[i])

print(dp[-1])