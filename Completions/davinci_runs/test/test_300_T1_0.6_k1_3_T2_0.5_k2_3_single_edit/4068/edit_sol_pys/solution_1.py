
import sys

# a[i] : i-th step is broken
N, M = [int(x) for x in sys.stdin.readline().split()]
a = []
for i in range(M):
    a.append(int(sys.stdin.readline()) - 1)

# dp[i] : i-th step can be reached by dp[i] ways
dp = [0 for i in range(N+1)]
dp[0] = 1
dp[1] = 0 if a[0] == 0 else 1

for i in range(2, N+1):
    # i-th step is not broken
    # dp[i] = dp[i-1] + dp[i-2]
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])
