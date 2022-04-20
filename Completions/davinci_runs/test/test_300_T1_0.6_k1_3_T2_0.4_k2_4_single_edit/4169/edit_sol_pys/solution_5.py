inf = float('inf')
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = [None] * n

for i in range(n):
    a, b = map(int, input().split())
    stores[i] = [a, b]

def solve():
    dp = [[[inf] * (m + 1) for _ in range(n)] for _ in range(2)]
    dp[0][0][0] = 0
    dp[0][0][1] = 0
#-----Solve-----
    for i in range(n):
        for j in range(m + 1):
            dp[0][i + 1][j] = min(dp[0][i + 1][j], dp[0][i][j])
            dp[1][i + 1][j] = min(dp[1][i + 1][j], dp[0][i][j] + stores[i][0])
            if j >= 1:
                dp[1][i + 1][j] = min(dp[1][i + 1][j], dp[1][i][j - 1] + stores[i][1])

    return dp[1][n][m]

print(solve())
#-----Display-----
