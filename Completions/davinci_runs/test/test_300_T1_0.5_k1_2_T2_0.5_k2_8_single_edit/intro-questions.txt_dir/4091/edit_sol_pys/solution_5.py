from collections import defaultdict


def f(n, k, a):
    dp = [defaultdict(int) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i < j:
                continue
            dp[i][j] = max(dp[i - l][j - 1] + max(a[i - l:i]) for l in range(1, min(k, i) + 1))

    ans = []
    i, j = n, k
    while j > 0:
        for l in range(1, min(k, i) + 1):
            if dp[i][j] == dp[i - l][j - 1] + max(a[i - l:i]):
                ans.append(l)
                i -= l
                j -= 1
                break

    return dp[n][k], ans[::-1]



n, k = map(int, input().split())
a = list(map(int, input().split()))

print(*f(n, k, a))
