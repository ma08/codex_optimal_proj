

import sys

# input
a, b, c = map(int, sys.stdin.readline().split())

# initialize
# dp = [[0] * (c + 1) for _ in range(c + 1)]
# dp[0][0] = 1
dp = [0] * (c + 1)
dp[0] = 1

# loop
for i in range(a, c + 1):
    for j in range(b, c + 1):
        dp[j] += dp[j - i]

# output result
print(dp[-1])
