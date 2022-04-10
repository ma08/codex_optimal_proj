

n = int(input())
a = list(map(int, input().split()))

# dp[i][j] = max length of increasing sequence with leftmost element a[i] and rightmost element a[j]
# dp[i][j] = 0 if i > j
# dp[i][j] = 1 if i == j
# dp[i][j] = dp[i][j - 1] + 1 if a[j] > a[j - 1]
# dp[i][j] = max(dp[i][k] + dp[k + 1][j]) for all k in [i, j) if a[j] < a[j - 1]

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if a[j] > a[j - 1]:
            dp[i][j] = dp[i][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][k] + dp[k + 1][j] for k in range(i, j))

print(dp[0][n - 1])

# reconstruct solution
i, j = 0, n - 1
solution = []
while i <= j:
    if a[j] > a[j - 1]:
        solution.append('R')
        j -= 1
    else:
        k = i
        while dp[i][j] != dp[i][k] + dp[k + 1][j]:
            k += 1
        solution.extend(['L'] * (k - i + 1))
        i = k + 1

print(''.join(solution))