

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = a[i - 1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        dp[i][j] = dp[i][j - 1] + a[j - 1]

# print(dp)

# dp[i][j] = k
# k - sum of elements from i to j
# dp[i][j] = dp[i][j - 1] + a[j - 1]

dp2 = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp2[i][i] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        dp2[i][j] = dp2[i][j - 1]

# print(dp2)

# dp2[i][j] = k
# k - number of blocks from i to j
# dp2[i][j] = dp2[i][j - 1]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(i, j):
            if dp[i][k] == dp[k + 1][j]:
                dp2[i][j] = max(dp2[i][j], dp2[i][k] + dp2[k + 1][j])

# print(dp2)

# dp2[i][j] = k
# k - max number of blocks from i to j
# dp2[i][j] = max(dp2[i][j], dp2[i][k] + dp2[k + 1][j])

# print(dp2)

print(dp2[1][n])

dp3 = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp3[i][i] = 1

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(i, j):
            if dp[i][k] == dp[k + 1][j]:
                if dp2[i][j] == dp2[i][k] + dp2[k + 1][j]:
                    dp3[i][j] = max(dp3[i][j], dp3[i][k] + dp3[k + 1][j])

# print(dp3)

# dp3[i][j] = k
# k - number of ways to get max number of blocks from i to j
# dp3[i][j] = max(dp3[i][j], dp3[i][k] + dp3[k + 1][j])

# print(dp3)

# print(dp3)

def print_blocks(i, j):
    if i == j:
        print(i, i)
        return
    for k in range(i, j):
        if dp[i][k] == dp[k + 1][j] and dp3[i][j] == dp3[i][k] + dp3[k + 1][j]:
            print_blocks(i, k)
            print_blocks(k + 1, j)
            return

print_blocks(1, n)