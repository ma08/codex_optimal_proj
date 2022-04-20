

def getMaxContest(arr):
    n = len(arr)
    dp = [1] * n  # dp[i] is the longest increasing subsequence ending at i
    for i in range(1, n):
        for j in range(i):
            if arr[i] <= 2 * arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)  # max of all dp[i]

a = list(map(int, input().split()))
print(getMaxContest(a))
