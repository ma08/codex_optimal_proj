

# SOLUTION
# Let's solve this problem using dynamic programming.
# We will store the answer in the following array:
#   dp[i][j] is the maximum possible sum of values of reposted pictures if we are at the end of the i-th segment of length k and we have reposted j pictures.
# The answer to our problem is dp[n][x].
#
# Now let's consider the following cases:
#   1. If i < k then we have not yet reached the first segment of length k.
#      In this case we can only repost the current picture and the answer is dp[i][j] = dp[i - 1][j - 1] + a_i.
#   2. If i = k then we have reached the first segment of length k.
#      In this case we have two options:
#        a. We can repost the current picture and the answer is dp[i][j] = dp[i - 1][j - 1] + a_i.
#        b. We can not repost the current picture and the answer is dp[i][j] = dp[i - k][j].
#   3. If i > k then we are in the middle of some segment of length k.
#      In this case we have two options:
#        a. We can repost the current picture and the answer is dp[i][j] = dp[i - 1][j - 1] + a_i.
#        b. We can not repost the current picture and the answer is dp[i][j] = dp[i - 1][j].
#
# We can calculate the answer for all values of i and j using these three cases.
# The answer to our problem is dp[n][x].
#
# Time Complexity: O(n * x)
# Space Complexity: O(n * x)

import sys
readline = sys.stdin.readline

n, k, x = map(int, readline().split())
a = list(map(int, readline().split()))

dp = [[0 for _ in range(x + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(i, x) + 1):
        if i < k:
            dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
        elif i == k:
            dp[i][j] = max(dp[i - 1][j - 1] + a[i - 1], dp[i - k][j])
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + a[i - 1], dp[i - 1][j])

if dp[n][x] == 0:
    print(-1)
else:
    print(dp[n][x])
