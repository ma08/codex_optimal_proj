

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(n + 1):
        if j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            for p in range(1, j + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - p] + max(a[j - p:j]))

print(dp[k][n])

ans = []
j = n
i = k
while i > 0:
    if dp[i][j] != dp[i - 1][j]:
        for p in range(1, j + 1):
            if dp[i - 1][j - p] + max(a[j - p:j]) == dp[i][j]:
                ans.append(p)
                j -= p
                break
    else:
        ans.append(0)
    i -= 1

print(*ans[::-1])