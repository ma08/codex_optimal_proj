

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

# dp[i][j] = maximum total profit for problems [i, j]
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    dp[i][i] = a[i]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        for m in range(i, j):
            dp[i][j] = max(dp[i][j], dp[i][m] + dp[m + 1][j])

# dp2[i][j] = maximum total profit for problems [i, j] and j - i + 1 days
dp2 = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    dp2[i][i] = a[i]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp2[i][j] = max(dp2[i][j - 1], dp2[i + 1][j])
        for m in range(i, j):
            dp2[i][j] = max(dp2[i][j], dp2[i][m] + dp[m + 1][j])

print(dp2[0][n - 1])

# dp3[i][j] = maximum total profit for problems [i, j] and j - i + 1 days and last day is i
dp3 = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    dp3[i][i] = a[i]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp3[i][j] = max(dp3[i][j - 1], dp3[i + 1][j])
        for m in range(i, j):
            dp3[i][j] = max(dp3[i][j], dp3[i][m] + dp[m + 1][j])

# ans[i][j] = maximum total profit for problems [i, j] and j - i + 1 days and last day is i and k days
ans = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    ans[i][i] = a[i]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        ans[i][j] = max(ans[i][j - 1], ans[i + 1][j])
        for m in range(i + 1, j + 1):
            ans[i][j] = max(ans[i][j], dp3[i][m - 1] + ans[m][j])

print(ans[0][n - 1])

# dp4[i][j] = maximum total profit for problems [i, j] and j - i + 1 days and last day is i and k days
dp4 = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    dp4[i][i] = a[i]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp4[i][j] = max(dp4[i][j - 1], dp4[i + 1][j])
        for m in range(i, j):
            dp4[i][j] = max(dp4[i][j], dp4[i][m] + dp[m + 1][j])

# ans[i][j] = maximum total profit for problems [i, j] and j - i + 1 days and last day is i and k days
ans = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    ans[i][i] = a[i]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        ans[i][j] = max(ans[i][j - 1], ans[i + 1][j])
        for m in range(i + 1, j + 1):
            ans[i][j] = max(ans[i][j], dp4[i][m - 1] + ans[m][j])

print(ans[0][n - 1])