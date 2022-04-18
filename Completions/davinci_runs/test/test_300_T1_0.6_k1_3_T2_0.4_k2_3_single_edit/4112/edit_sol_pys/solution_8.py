

n, k, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

def dp(n, k, x, a):
    if x == 0 or n == k:
        return sum(a)

    dp = [[[-1 for _ in range(x+1)] for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(k):
            dp[i][j][1] = sum(a[i:i+j])

    for i in range(n):
        for j in range(k+1):
            for l in range(2, x+1):
                for m in range(i+j, n):
                    if j+m-i >= k:
                        dp[i][j][l] = max(dp[i][j][l], sum(a[i:i+j])+dp[m][j+m-i-k][l-1])

    return max([max(x) for x in dp[0][0][1:]])

print(dp(n, k, x, a))
