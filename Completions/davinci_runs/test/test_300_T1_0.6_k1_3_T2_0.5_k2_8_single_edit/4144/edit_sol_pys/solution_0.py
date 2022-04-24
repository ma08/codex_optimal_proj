

import numpy as np

n = int(input()) + 1

# dp[i][j][k] i桁目まででjが出てきた回数で、i桁目がkであるものの個数 mod (10^9 + 7)
dp = np.zeros((n, n, 2), dtype=np.int64)
dp[0][0][0] = 1 % (10**9 + 7)
dp[0][0][1] = 0 % (10**9 + 7)
dp[0][1][0] = 0 % (10**9 + 7)
dp[0][1][1] = 1 % (10**9 + 7)

for i in range(1, n-1):
    for j in range(n-1):
        if j == 0:
            dp[i][j][0] %= (10**9 + 7)
            dp[i][j][1] = dp[i-1][j][1] % (10**9 + 7)
        elif j == n-2:
            dp[i][j][0] = dp[i-1][j][0] * 9 + dp[i-1][j-1][1]
            dp[i][j][0] %= (10**9 + 7)
            dp[i][j][1] = dp[i-1][j][1] % (10**9 + 7)
        else:
            dp[i][j][0] = dp[i-1][j][0] * 8 + dp[i-1][j+1][1] + dp[i-1][j-1][1]
            dp[i][j][1] = dp[i-1][j][1]
ans = sum(dp[n-1][j][0] for j in range(n))
print(ans % (10**9 + 7))
