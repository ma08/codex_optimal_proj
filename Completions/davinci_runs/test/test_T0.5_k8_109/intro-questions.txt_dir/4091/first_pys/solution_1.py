

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i-1], a[i-1])

ans = [0] * k

for i in range(k-1, 0, -1):
    for j in range(i, n+1):
        if dp[j] - dp[j-i] > dp[n] - dp[n-i]:
            dp[j] = dp[j-i]
            ans[i-1] = j - i
            n = j
            break

print(dp[n])

for i in range(k):
    if i == 0:
        print(ans[i]+1)
    else:
        print(ans[i]-ans[i-1])