

import sys

# Read the input
N, A, B, C = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for i in range(N)]

# dp[n][a][b][c] is the minimum amount of MP needed to obtain three bamboos of lengths a, b, c from n bamboos.
dp = [[[[float("inf") for c in range(C+1)] for b in range(B+1)] for a in range(A+1)] for n in range(N+1)]
dp[0][0][0][0] = 0

for i in range(N):
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                # Do nothing
                dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c])
                # Extend a bamboo
                if a >= l[i]:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a-l[i]][b][c] + 1)
                if b >= l[i]:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b-l[i]][c] + 1)
                if c >= l[i]:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c-l[i]] + 1)
                # Shorten a bamboo
                if a + l[i] <= A:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a+l[i]][b][c] + 1)
                if b + l[i] <= B:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b+l[i]][c] + 1)
                if c + l[i] <= C:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c+l[i]] + 1)
                # Combine two bamboos
                if a + l[i] <= A:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a+l[i]][b][c] + 10)
                if b + l[i] <= B:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b+l[i]][c] + 10)
                if c + l[i] <= C:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c+l[i]] + 10)

# Print the answer
print(dp[N][A][B][C])
