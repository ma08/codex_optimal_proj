
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    n = len(a)
    dp = [[1, 1] for _ in range(n)]
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            dp[i][0] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
            dp[i][1] = dp[i - 1][1] + 1
        else:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
    return max(dp[n - 1][0], dp[n - 1][1])

print(solve(a))
