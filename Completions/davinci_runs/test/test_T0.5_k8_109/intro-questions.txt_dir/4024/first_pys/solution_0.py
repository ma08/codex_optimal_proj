

# SOLUTION
# We can use dynamic programming to solve this problem. Let dp[i][j] be the minimum cost for the first i characters,
# and j subsequences.
# The base case is dp[0][0] = 0, because for the empty string, there is no cost to create the first subsequence.
# The recurrence relation is dp[i][j] = min(dp[i][j], dp[i-k][j-1] + i-k), where k is a subsequence of the first i characters.
# We can use a binary search to find the maximum length of a subsequence, and then use a prefix sum to find the cost.
# The time complexity is O(n^2 * log(n)), and the space complexity is O(n^2).

import sys
from bisect import bisect_right

input = sys.stdin.readline

n, k = map(int, input().split())
s = input()

dp = [[float('inf') for j in range(k+1)] for i in range(n+1)]
dp[0][0] = 0

prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + i

for i in range(1, n+1):
    for j in range(1, min(i+1, k+1)):
        dp[i][j] = min(dp[i][j], dp[i-1][j-1] + i)
        l = 1
        r = i+1
        while l < r:
            m = (l+r) // 2
            if s[i-m:i] == s[i-m:i-m+m]:
                l = m+1
            else:
                r = m
            dp[i][j] = min(dp[i][j], dp[i-l][j-1] + (prefix_sum[i] - prefix_sum[i-l]))

if dp[n][k] == float('inf'):
    print(-1)
else:
    print(dp[n][k])