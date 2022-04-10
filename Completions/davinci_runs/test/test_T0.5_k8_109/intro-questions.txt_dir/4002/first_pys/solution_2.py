

# Solution

n, m, k = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# dp[i][j][k] = maximum sum of elements in the first i rows with j elements in the last row and the sum is divisible by k
dp = [[[0 for _ in range(k)] for _ in range(m // 2 + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m // 2 + 1):
        for l in range(k):
            dp[i][j][l] = dp[i - 1][j][l]
            if j <= m - j:
                dp[i][j][l] = max(dp[i][j][l], dp[i - 1][j - 1][(l - matrix[i - 1][j - 1]) % k] + matrix[i - 1][j - 1])
            if j <= m - j + 1:
                dp[i][j][l] = max(dp[i][j][l], dp[i - 1][j][(l - matrix[i - 1][m - j]) % k] + matrix[i - 1][m - j])

print(dp[n][m // 2][0])