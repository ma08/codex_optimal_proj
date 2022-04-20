

n,k,x = [int(x) for x in input().split()] # n = length of array, k = length of subarray, x = number of swaps
a = [int(x) for x in input().split()] # array

def brute_force(n, k, x, a): # time limit exceeded
    if x == 0:
        return 0
    if n == k:
        return sum(a)
    max_sum = -1
    for i in range(n-k+1):
        curr_sum = sum(a[i:i+k])
        curr_sum += brute_force(n-k, k, x-1, a[i+k:])
        max_sum = max(max_sum, curr_sum)
    return max_sum

def dp(n, k, x, a): # accepted
    if x == 0:
        return 0
    if n == k:
        return sum(a)

    dp = [[[-1 for _ in range(x+1)] for _ in range(k)] for _ in range(n)] # dp[i][j][l] = max sum of subarrays of length j starting from index i with l swaps

    for i in range(n):
        for j in range(k):
            if i+j >= n:
                break
            dp[i][j][1] = sum(a[i:i+j+1]) # base case
    
    for i in range(n):
        for j in range(k):
            if i+j >= n:
                break
            for l in range(2, x+1):
                for m in range(i+j+1, n):
                    if j+m-i+1 >= k:
                        dp[i][j][l] = max(dp[i][j][l], sum(a[i:i+j+1])+dp[m][j+m-i+1-k][l-1]) # recursive case
    
    return max([max(x) for x in dp[0][0]]) # return max sum of subarrays of length 0 starting from index 0 with l swaps

#print(brute_force(n,k,x,a))
print(dp(n,k,x,a))
