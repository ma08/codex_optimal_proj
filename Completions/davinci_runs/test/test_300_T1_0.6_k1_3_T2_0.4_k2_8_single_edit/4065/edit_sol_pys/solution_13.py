
def getMaxContest(a):
    n = len(a)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] <= 2 * a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


a = list(map(int, input().split()))
print(getMaxContest(a))
