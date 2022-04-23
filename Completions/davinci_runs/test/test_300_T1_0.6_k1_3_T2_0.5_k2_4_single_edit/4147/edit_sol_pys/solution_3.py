

import sys

# Read the input
N, A, B, C = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for i in range(N)]

# dp[n][a][b][c] is the minimum amount of MP needed to obtain three bamboos of lengths a, b, c from n bamboos
dp = [[[[float("inf") for i in range(C+1)] for j in range(B+1)] for k in range(A+1)] for l in range(N+1)]
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
                # Extend b bamboo
                if b >= l[i]:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b-l[i]][c] + 1)
                # Extend c bamboo
                if c >= l[i]:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c-l[i]] + 1)
                # Shorten an a bamboo
                if a + l[i] <= A:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a+l[i]][b][c] + 1)
                # Shorten a b bamboo
                if b + l[i] <= B:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b+l[i]][c] + 1)
                # Shorten a c bamboo
                if c + l[i] <= C:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c+l[i]] + 1)
                # Combine two a bamboos
                if a + l[i] <= A:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a+l[i]][b][c] + 10)
                # Combine two b bamboos
                if b + l[i] <= B:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b+l[i]][c] + 10)
                # Combine two c bamboos
                if c + l[i] <= C:
                    dp[i+1][a][b][c] = min(dp[i+1][a][b][c], dp[i][a][b][c+l[i]] + 10)

# Print the answer
print(dp[N][A][B][C])
