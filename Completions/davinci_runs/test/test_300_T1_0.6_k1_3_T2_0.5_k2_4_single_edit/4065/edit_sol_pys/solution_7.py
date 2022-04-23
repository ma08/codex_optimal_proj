

def getMaxContest(A):
    n = len(A)
    dp = [1] * n # dp[i] = longest increasing subsequence ending at index i
    for i in range(1, n):
        for j in range(i):
            if A[i] <= 2 * A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) # return the maximum of dp

a = list(map(int, input().split()))
print(getMaxContest(a))
