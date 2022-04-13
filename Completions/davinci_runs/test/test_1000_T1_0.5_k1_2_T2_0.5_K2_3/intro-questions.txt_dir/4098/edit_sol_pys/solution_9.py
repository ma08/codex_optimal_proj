

# n, k = map(int, input().split())


def solve(a, k):  # naive O(n^2 * k)
    a.sort()
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            t = 1
            for l in range(1, i):
                if abs(a[i - 1] - a[i - l - 1]) <= 5:
                    t += 1
                else:
                    break
            dp[i][j] = max(dp[i][j], dp[i - t][j - 1] + t)
    return dp[n][k]

# a = list(map(int, input().split()))

n, k = 5, 2
a = [1, 2, 15, 15, 15]
# n, k = 6, 1
# a = [36, 4, 1, 25, 9, 16]
# n, k = 4, 4
# a = [1, 10, 100, 1000]


print(solve(a, k))
