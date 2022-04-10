

n,m,k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

def max_sum(a, k):
    dp = [[0] * (m//2 + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m//2 + 1):
            if j > i:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1][j-1])
    return dp[n][m//2]

def max_sum_divisible(a, k):
    max_sum = 0
    for i in range(n):
        for j in range(m//2 + 1):
            max_sum += a[i][j]
    for i in range(n):
        for j in range(m//2 + 1):
            for l in range(j+1, m//2 + 1):
                max_sum = max(max_sum, max_sum(a[i][j:l], k))
    return max_sum

print(max_sum_divisible(a, k))