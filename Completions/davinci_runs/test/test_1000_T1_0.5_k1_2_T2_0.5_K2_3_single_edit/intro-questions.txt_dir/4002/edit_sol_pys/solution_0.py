
n, m, k = map(int, input().split())
a = [0]
for i in range(n):
    a += list(map(int, input().split()))

dp = [0 for i in range(m+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j >= m//2 and j > 0:
            dp[j] = max(dp[j], dp[j-1] + a[i*m + j])
        else:
            dp[j] = dp[j]

print(dp[n][m])
