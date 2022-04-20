

import sys
input = sys.stdin.readline

n = int(input())

# dp[i][j][k] i桁目まででjが出てきた回数で、i桁目がkであるものの個数 k = 0: 0, 1: 1
# i桁目が0のときはjが出てきた回数がj-1になる
# i桁目が9のときはjが出てきた回数がj+1になる
# それ以外のときはjが出てきた回数はj-1, j, j+1のいずれかになる
dp = [[[0]*2 for _ in range(n+1)] for _ in range(n+1)]
# 1桁目は0のときしかない
dp[0][0][0] = 1
dp[0][0][1] = 0
# 1桁目は1のときしかない
dp[0][1][0] = 0
dp[0][1][1] = 1

for i in range(1, n):
    for j in range(n):
            # 0の時はj-1回
        if j == 0:
            # 1の時はj回
            dp[i][j][0] = dp[i-1][j][0] * 8 + dp[i-1][j+1][1]
            dp[i][j][1] = dp[i-1][j][1]
        elif j == n-1:
            # 0の時はj回
            dp[i][j][0] = dp[i-1][j][0] * 9 + dp[i-1][j-1][1]
            # 1の時はj回
            dp[i][j][1] = dp[i-1][j][1]
        else:
            # 0の時はj-1回
            dp[i][j][0] = dp[i-1][j][0] * 8 + dp[i-1][j+1][1] + dp[i-1][j-1][1]
            # 1の時はj回
            dp[i][j][1] = dp[i-1][j][1]
ans = sum(dp[n-1][j][0] for j in range(n))
print(ans % (10**9 + 7))
