

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # dp[i][j] means max profit from first i problems, divided into j groups
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # max_profit[i][j] means max profit from a[i] to a[j - 1]
    max_profit = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        max_profit[i][i + 1] = a[i]
        for j in range(i + 2, n + 1):
            max_profit[i][j] = max(max_profit[i][j - 1], a[j - 1])

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i >= j:
                for l in range(0, i - j + 2):
                    dp[i][j] = max(dp[i][j], dp[l][j - 1] + max_profit[l][i - 1])

    print(dp[n][k])

    groups = []
    group_size = []
    i, j = n, k
    while i > 0 and j > 0:
        for l in range(0, i - j + 2):
            if dp[i][j] == dp[l][j - 1] + max_profit[l][i - 1]:
                groups.append((l, i - 1))
                group_size.append(i - l)
                i, j = l, j - 1
                break

    for g in reversed(groups):
        print(max(a[g[0]:g[1]]), end=' ')

solve()
