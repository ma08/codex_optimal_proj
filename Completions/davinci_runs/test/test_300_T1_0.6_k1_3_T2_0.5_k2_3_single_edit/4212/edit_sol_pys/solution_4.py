

from collections import deque

n, m, q = map(int, input().split())

# a_i, b_i, c_i, d_i
quads = [list(map(int, input().split())) for _ in range(q)]

# dp[i][j] ... maximum score for first i numbers with last number equal j
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    # if we don't use the last number
    dp[i][0] = dp[i-1][0]

    # if we use the last number
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1]

        # check if we can contribute with the last number
        for a, b, c, d in quads:
            if a == i and b == j:
                dp[i][j] = max(dp[i][j], dp[i-1][c-1] + d)

print(max(dp[n]))
