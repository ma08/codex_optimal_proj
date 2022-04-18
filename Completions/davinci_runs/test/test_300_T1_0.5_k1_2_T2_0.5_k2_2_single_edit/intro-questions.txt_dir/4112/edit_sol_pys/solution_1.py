

n, k, x = map(int, input().split())
pictures = list(map(int, input().split()))

# print(n, k, x)
# print(pictures)

# dp[i][j] = max sum of pictures from range [i, j] inclusive
# with j - i >= k
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = pictures[i]

for width in range(1, n):
    for i in range(n - width):
        j = i + width
        if j - i + 1 < k:
            dp[i][j] = 0
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], dp[i][j - 1] + pictures[j], dp[i + 1][j - 1] + pictures[j])

# for row in dp:
#     print(row)

if x == n:
    print(dp[0][n - 1])
elif x > n:
    print(-1)
else:
    # dp[i][j] = max sum of pictures from range [i, j] inclusive
    # with j - i >= k and j - i >= x
    dp2 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp2[i][i] = pictures[i]

    for width in range(1, n):
        for i in range(n - width):
            j = i + width
            if j - i + 1 < k or j - i + 1 < x:
                dp2[i][j] = 0
            else:
                dp2[i][j] = max(dp2[i][j - 1], dp2[i + 1][j], dp2[i][j - 1] + pictures[j], dp2[i + 1][j - 1] + pictures[j])

    # for row in dp2:
    #     print(row)

    print(dp2[0][n - 1])
