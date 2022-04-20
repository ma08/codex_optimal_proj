

import sys

N, M = [int(x) for x in sys.stdin.readline().split()]
a = []
for i in range(M):
    a.append(int(sys.stdin.readline()))

# a[i] : i-th step is broken
# a[i] = 1 : i-th step is broken, a[i] = 0 : i-th step is not broken
a = [1 if a[i] in a else 0 for i in range(N)]

# dp[i] : i-th step can be reached by dp[i] ways
dp = [0 for i in range(N+1)]
dp[0] = 1
dp[1] = 1 if a[0] == 0 else 0

for i in range(2, N+1):
    # if i-th step is broken
    if a[i-1] == 1:
        dp[i] = 0
    else:
        # i-th step is not broken
        # dp[i] = dp[i-1] + dp[i-2]
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])
