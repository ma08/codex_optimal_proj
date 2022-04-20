

# --- Input --- #
N, M, Q = map(int, input().split())

# --- Initialization --- #
a, b, c, d = [], [], [], []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

# --- Main --- #
# dp[i][j] : maximum score of a sequence whose length is i and the maximum value is j
dp = [[0 for i in range(M+1)] for j in range(N+1)]

# Initialization
for i in range(N+1):
    for j in range(M+1):
        for k in range(Q):
            if i == a[k] and j == c[k] + 1:
                dp[i][j] = d[k]

# Update
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        for k in range(Q):
            if i == b[k] and j == c[k] + 1:
                dp[i][j] = max(dp[i][j], dp[a[k]][j-c[k]] + d[k])

print(dp[N][M])