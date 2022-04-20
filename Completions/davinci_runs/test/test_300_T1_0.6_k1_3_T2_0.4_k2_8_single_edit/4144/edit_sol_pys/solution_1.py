import sys
input = sys.stdin.readline().rstrip()

n = int(input())

# dp[i][j] i桁目まででjが出てきた回数であるものの個数
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
dp[0][1] = 0

for i in range(1, n+1):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j] * 8 + dp[i-1][j+1]
        elif j == n-1:
            dp[i][j] = dp[i-1][j] * 9 + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j] * 8 + dp[i-1][j+1] + dp[i-1][j-1]
ans = sum(dp[n][j] for j in range(n))
print(ans % (10**9 + 7))
