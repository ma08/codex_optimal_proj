

def getMaxContest(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] <= 2 * arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

arr = list(map(int, input().split()))
print(getMaxContest(arr))
