

a, n, m = map(int, input().split())

segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

umbrellas = []
for _ in range(m):
    x, p = map(int, input().split())
    umbrellas.append((x, p))

# print(a, n, m)
# print(segments)
# print(umbrellas)

# dp[i][j] = min fatigue if we start at segment i and have umbrella j
dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

# base case: no segments and no umbrellas
dp[0][0] = 0

for i in range(n):
    l, r = segments[i]
    for j in range(m + 1):
        x, p = umbrellas[j - 1] if j > 0 else (0, 0)
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if l <= x <= r:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + p)
        if l <= x + 1 <= r:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + p)

# print(dp)

# find min of all possible final states
ans = min(dp[n][j] for j in range(m + 1))

print(ans)