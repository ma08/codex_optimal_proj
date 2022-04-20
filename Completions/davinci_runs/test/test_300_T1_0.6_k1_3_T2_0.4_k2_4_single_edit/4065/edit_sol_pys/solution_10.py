

def getMaxContest(arr):
    n = len(arr)
    dp = [1] * n #dp[i] = the longest increasing subsequence ending at arr[i]
    for i in range(n): #iterate through all the elements
        for j in range(i): #compare with all the elements before it
            if arr[i] <= 2 * arr[j]: #if arr[i] is less than 2 times the value of arr[j]
                dp[i] = max(dp[i], dp[j] + 1) #update dp[i] with the max of its current value and dp[j] + 1
    return max(dp) #return the max value in dp array

a = list(map(int, input().split()))
print(getMaxContest(a))
