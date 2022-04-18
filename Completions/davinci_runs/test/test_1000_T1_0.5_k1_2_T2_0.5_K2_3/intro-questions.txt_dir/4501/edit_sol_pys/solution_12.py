
import sys


def read_ints():
    return list(map(int, sys.stdin.readline().split()))


n, a = read_ints()
x = [0] + read_ints()

# dp[i][j][k] := i番目までのカードからj枚選んで合計がkになる通り数。
dp = [[[0] * (n * 50 + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1  # 1通り

for i in range(n):
    for j in range(n):
        for k in range(n * 50 + 1):
            dp[i + 1][j][k] += dp[i][j][k]
            if j + 1 <= n and k + x[i + 1] <= n * 50:
                dp[i + 1][j + 1][k + x[i]] += dp[i][j][k]

print(dp[n][n // 2][a * n // 2])
