

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] = maximum sum of values of reposted pictures if Vova follows conditions described in the problem statement
# and he has already reposted j pictures in the first i pictures.
dp = [[0 for _ in range(x+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, min(i, x)+1):
        # if we don't repost the i-th picture
        dp[i][j] = dp[i-1][j]
        # if we repost the i-th picture
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1])
        # if we repost the i-th picture and some pictures in the previous k-1 pictures
        for l in range(max(j-1, 1), min(i-k+1, x)):
            dp[i][j] = max(dp[i][j], dp[i-k][l] + a[i-1])

print(dp[n][x] if dp[n][x] != 0 else -1)