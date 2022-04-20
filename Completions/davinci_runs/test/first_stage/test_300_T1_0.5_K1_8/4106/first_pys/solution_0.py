

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] = maximum sum of values of reposted pictures for the first i pictures with j reposts
dp = [[0 for _ in range(x+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, x+1):
        # if we don't repost the i-th picture, then we can repost any number of pictures from the first i-1 pictures
        dp[i][j] = dp[i-1][j]
        # if we repost the i-th picture, then we can repost at most j-1 pictures from the first i-1 pictures
        for p in range(1, min(i, j)):
            # if the i-th picture is the first picture in a segment of length k
            if i-p < k:
                dp[i][j] = max(dp[i][j], dp[i-p-1][j-p] + a[i-1])
            # if the i-th picture is not the first picture in a segment of length k
            else:
                dp[i][j] = max(dp[i][j], dp[i-p][j-p] + a[i-1])

if dp[n][x] == 0:
    print(-1)
else:
    print(dp[n][x])