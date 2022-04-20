n = int(input())
a = list(map(int, input().split()))


dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    if i - a[i] >= 0:
        dp[i] = max(dp[i - a[i]], dp[i - a[i] + 1])
    else:
        dp[i] = dp[i - a[i] + 1]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            ans = max(ans, dp[i] + 1 + dp[j])
        else:
            ans = max(ans, dp[i] + 1)

print(ans)
