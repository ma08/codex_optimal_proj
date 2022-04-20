

n, k = map(int, input().split())
a = list(map(int, input().split()))

"""
dp[i][j] means the maximum total profit, if we solve the first i problems in j days.

dp[i][j] = max(dp[i-1][j], max(dp[i-k][j-1], dp[i-k-1][j-1], ..., dp[i-2][j-1], dp[i-1][j-1]) + max(a[i-k], a[i-k+1], ..., a[i-1]))
"""
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# max_sum[i] means the maximum sum of the last i numbers.
max_sum = [0 for _ in range(n+1)]

for i in range(1, n+1):
    max_sum[i] = max(max_sum[i-1], 0) + a[i-1]
    for j in range(1, k+1):
        if i >= j:
            dp[i][j] = max(dp[i-1][j], max_sum[i] - max_sum[i-j])

ans = dp[n][k]

res = [0 for _ in range(k)]
i, j = n, k
while i > 0:
    while i >= j and dp[i][j] == dp[i-1][j]:
        i -= 1
    if i < j:
        break
    res[j-1] += 1
    i -= j

print(ans)
print(' '.join(map(str, res)))