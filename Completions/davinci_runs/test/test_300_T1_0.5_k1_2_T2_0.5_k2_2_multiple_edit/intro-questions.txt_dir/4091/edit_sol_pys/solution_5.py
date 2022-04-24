

n, k = map(int, input().split()) # n = number of problems, k = number of days
a = list(map(int, input().split())) # a = list of problems

# dp[i][j] = max profit for i problems in j days.
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# dp[i][j] = max(dp[i - 1][j - 1] + max(a[i - 1:]), dp[i - 2][j - 1] + max(a[i - 2:])...dp[i - k][j - 1] + max(a[i - k:]))
# dp[i][j] = max(dp[i - l][j - 1] + max(a[i - l:i]) for l in range(1, min(k, i) + 1))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i < j:
            continue
        dp[i][j] = max(dp[i - l][j - 1] + max(a[i - l:i]) for l in range(1, min(k, i) + 1)) # min(k, i) because we can't use more than k days for i problems

print(dp[n][k]) # max profit

i, j = n, k # starting from the bottom right corner of the dp table
ans = []
while j > 0:
    for l in range(1, min(k, i) + 1):
        if dp[i][j] == dp[i - l][j - 1] + max(a[i - l:i]): # when we reach the optimal solution for i problems in j days, we get the number of problems solved in the jth day
            ans.append(l)
            i -= l
            j -= 1
            break

print(*ans[::-1]) # print the days in reverse order
