

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
n, k = 5, 2
a = [1, 2, 5, 10, 15]
# n, k = 6, 1
# a = [36, 4, 1, 25, 9, 16]
# n, k = 4, 4
# a = [1, 10, 100, 1000] # 1


def solve(a, k):
    a.sort()
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, k + 1):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            if abs(a[i - 1] - a[j - 1]) <= 5:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
        for j in range(2, k + 1):
            for l in range(1, i):
                if abs(a[i - 1] - a[l - 1]) <= 5:
                    dp[i][j] = max(dp[i][j], dp[l][j - 1] + 1)
    return max(dp[n])


print(solve(a, k))
