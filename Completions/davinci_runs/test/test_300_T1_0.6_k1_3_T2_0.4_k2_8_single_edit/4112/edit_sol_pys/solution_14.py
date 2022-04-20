

n, k = map(int, input().split())

arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

# dp[i][j] is the max sum of beauty values of pictures that
# can be posted from index i to j
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = arr[i][0]
    if i+1 < n:
        dp[i][i+1] = max(arr[i][0], arr[i+1][0])

for i in range(n-2, -1, -1):
    for j in range(i+2, n):
        dp[i][j] = max(
            dp[i+1][j],
            dp[i][j-1],
            dp[i+1][j-1] + arr[j][1]
        )

print(dp[0][n-1])
