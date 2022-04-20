
n, k, x = map(int, input().split())
pictures = list(map(int, input().split()))  # pictures[i] = number of pictures in i-th file

# dp[i][j] = max sum of pictures from range [i, j] with j - i >= k
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = pictures[0]

if x == n:
    print(dp[0][0])
elif x > n:
    print(-1)
else:
    # dp[i][j] = max sum of pictures from range [i, j] with j - i >= k and j - i >= x
    dp2 = [[0 for _ in range(n)] for _ in range(n)]

    dp2[0][0] = pictures[0]

    for width in range(1, n):  # width = j - i
        for i in range(n - width):
            j = i + width
            if j - i + 1 < k or j - i + 1 < x:
                dp2[i][j] = 0
            else:
                dp2[i][j] = max(dp2[i][j - 1], dp2[i + 1][j], dp2[i][j - 1] + pictures[j])

                dp2[i][j] = max(dp2[i][j - 1], dp2[i + 1][j], dp2[i][j - 1] + pictures[j])

    print(dp2[0][n - 1])  # dp2[0][n - 1] = max sum of pictures from range [0, n - 1]
