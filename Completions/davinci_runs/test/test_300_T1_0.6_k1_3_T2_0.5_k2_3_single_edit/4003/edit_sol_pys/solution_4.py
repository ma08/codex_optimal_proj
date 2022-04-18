n = int(input())
arr = [int(x) for x in input().split()]



def solve(arr):
    n = len(arr)
    dp = [[0, 0] for i in range(n)]
    dp[0][0] = 1  # increasing
    dp[0][1] = 1  # decreasing
    for i in range(1, n):  # for each index
        if arr[i] > arr[i - 1]:  # increasing
            dp[i][0] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
            dp[i][1] = dp[i - 1][1] + 1
        else:  # decreasing
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
    return max(dp[n - 1][0], dp[n - 1][1])  # return longest subsequence

print(solve(a))
