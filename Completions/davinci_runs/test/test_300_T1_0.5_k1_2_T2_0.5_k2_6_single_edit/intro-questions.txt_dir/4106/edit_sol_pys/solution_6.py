
def solve(n, a):
    if n == 0:
        return 0
    elif n == 1:
        return a[0]
    elif n == 2:
        return a[0] + a[1]
    else:
        dp = [0]*n
        dp[0] = a[0]
        dp[1] = a[0] + a[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+a[i])
        return dp[n-1]
