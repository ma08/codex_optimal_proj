def max_subarray(a):
    dp = [0] * len(a)
    dp[0] = a[0]
    for i in range(1, len(a)):
        dp[i] = max(dp[i - 1] + a[i], a[i])
    return max(dp)
