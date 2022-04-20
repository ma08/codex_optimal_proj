
n, k = map(int, raw_input().split())
s = raw_input()

# The idea is to find the optimal solution for the first i elements
# and the first j subsequences.

# dp[i][j] holds the optimal solution for the first i elements
# and the first j subsequences.

dp = [[0 for j in range(k + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        # If it is possible to create j subsequences
        # using the first i elements, we can create
        # j subsequences using the first i - 1 elements,
        # and one subsequence of size i.
        # This subsequence costs i - 1.
        if j * (j + 1) / 2 <= i:
            dp[i][j] = min(dp[i][j], i - 1 + dp[i - 1][j - 1])

        # If it is possible to create j subsequences
        # using the first i - 1 elements, we can create
        # j subsequences using the first i elements,
        # by skipping the ith element.
        # This subsequence costs 0.
        dp[i][j] = min(dp[i][j], dp[i - 1][j])

# If it is possible to create k subsequences using the first n elements,
# print the optimal solution. Otherwise, print -1.
if dp[n][k] != 0:
    print dp[-1][-1]
else:
    print -1
