import sys
input = sys.stdin.readline


n, k, x = map(int, input().strip().split())
pictures = list(map(int, input().strip().split()))

# print(n, k, x)
# print(pictures)

# dp[i][j] = max sum of pictures from range [i, j]
# with j - i >= k
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    dp[i][i + 1] = pictures[i]

for width in range(2, n + 1):
    for i in range(n + 1 - width):
        j = i + width - 1
        dp[i][j + 1] = max(dp[i][j], dp[i + 1][j + 1], dp[i][j] + pictures[j])

# for row in dp:
#     print(row)

if x == n:
    print(dp[0][n])
elif x > n:
    print(-1)
else:
    # dp[i][j] = max sum of pictures from range [i, j]
    # with j - i >= k and j - i >= x
    dp2 = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        dp2[i][i + 1] = pictures[i]

    for width in range(2, n + 1):
        for i in range(n + 1 - width):
            j = i + width - 1
            dp2[i][j + 1] = max(dp2[i][j], dp2[i + 1][j + 1], dp2[i][j] + pictures[j])

    # for row in dp2:
    #     print(row)

    print(dp2[0][n])
