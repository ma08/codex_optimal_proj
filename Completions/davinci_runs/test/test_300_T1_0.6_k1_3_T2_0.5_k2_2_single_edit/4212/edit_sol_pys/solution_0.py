

n = int(input())

a = list(map(int, input().split()))

dp = [0] * n

dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

    # if we use the last number
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1]

        # check if we can contribute with the last number
        for a, b, c, d in quads:
            if a == i and b == i+1 and c == j:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + d)

print(max(dp[n]))
