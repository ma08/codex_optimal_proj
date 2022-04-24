

def getMaxContest(a, n):
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i + 1):
            if a[i] <= 2 * a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

a = list(map(int, input().split()))
print(getMaxContest(a))
