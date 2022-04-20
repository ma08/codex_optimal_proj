

def solve_dp(n, a, b):
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i + j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i - 1][j] + a[i - 1], dp[i][j - 1] + b[j - 1])
    return dp[n - 1][n - 1]


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(solve_dp(n, a, b))
