

def max_profit(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i < j:
        dp[i][j] = 0
        return dp[i][j]
    dp[i][j] = max(max_profit(i - l, j - 1) + max(a[i - l:i]) for l in range(1, min(k, i) + 1))
    return dp[i][j]


def max_profit_sequence(i, j):
    if j == 0:
        return []
    for l in range(1, min(k, i) + 1):
        if dp[i][j] == dp[i - l][j - 1] + max(a[i - l:i]):
            return max_profit_sequence(i - l, j - 1) + [l]


n, k = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] = max profit for i problems in j days
dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

print(max_profit(n, k))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i < j:
            continue
        dp[i][j] = max(dp[i - l][j - 1] + max(a[i - l:i]) for l in range(1, min(k, i) + 1))

print(dp[n][k])

i, j = n, k
ans = []
while j > 0:
    for l in range(1, min(k, i) + 1):
        if dp[i][j] == dp[i - l][j - 1] + max(a[i - l:i]):
            ans.append(l)
            i -= l
            j -= 1
            break

print(*ans[::-1])
