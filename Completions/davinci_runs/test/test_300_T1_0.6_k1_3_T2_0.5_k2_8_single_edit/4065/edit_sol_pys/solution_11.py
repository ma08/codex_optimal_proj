

def getMaxContest(a, n):
    dp = [1] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i):
            if a[i] <= 2 * a[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp[1:])

n = int(input())
a = [0] + list(map(int, input().split()))
print(getMaxContest(a, n))
