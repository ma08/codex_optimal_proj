

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

def solve(n, h, l, r, a):
    dp = [[0] * h for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(h):
            dp[i][j] = dp[i-1][j]
            if j >= a[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-a[i-1]])
            if j >= a[i-1] - 1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-a[i-1]+1])
    return sum(dp[n][l:r+1])

print(solve(n, h, l, r, a))
