
# https://www.hackerrank.com/challenges/maximize-it/problem


n,k,x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

def brute_force(n, k, x, a):
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

def dp(n, k, x, a):
    if x == 0:
        return 0
    if n == k:
        return sum(a)

    dp = [[[-1 for _ in range(x+1)] for _ in range(k)] for _ in range(n)]

        return sum(a) * x

    dp = [[[-1 for _ in range(x+1)] for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(k+1, i+1)):
            dp[i][j][1] = sum(a[i-j:i])

    for i in range(1, n+1):
        for j in range(1, min(k+1, i+1)):
            for l in range(2, min(x+1, i-j+2)):
                dp[i][j][l] = dp[i-1][j][l]
                for m in range(1, j+1):
                    dp[i][j][l] = max(dp[i][j][l], dp[i-m][j][l-1]+sum(a[i-j:i]))

    return max([max(x) for x in dp[n][k]])

#print(brute_force(n,k,x,a))
print(dp(n,k,x,a))
