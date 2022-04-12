
import sys


def read_ints():
    return list(map(int, sys.stdin.readline().split()))


N, A = read_ints()
x = read_ints()

# dp[i][j][k] := i枚目までのカードからj枚選んで合計がkになる通り数
dp = [[[0] * (50 * 50 + 1) for _ in range(50 + 1)] for _ in range(51)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(50 * 50 + 1):
            dp[i + 1][j][k] += dp[i][j][k]
            if j + 1 <= N and k + x[i] <= 50 * 50:
                dp[i + 1][j + 1][k + x[i]] += dp[i][j][k]

print(dp[N][N][A * N])
