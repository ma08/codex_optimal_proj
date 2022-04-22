

from sys import stdin, stdout

n, m = map(int, stdin.readline().strip().split())

# adjacency matrix
adj = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, stdin.readline().strip().split())
    u -= 1
    v -= 1
    adj[u][v] = 1
    adj[v][u] = 1

# calculate all the colorings
# we use a bitmask to represent the colorings
# for example, 11001 represents that vertices 1, 2, and 4 are colored red,
# while vertices 3 and 5 are colored blue
# use dp with bitmask to represent state
dp = [[0] * (2 ** n) for _ in range(n)]
dp[0][1] = 1

MOD = 10**9 + 7
for i in range(1, 2 ** n):
    for u in range(n):
        if i & (1 << u) == 0:
            continue
        for v in range(n):
            if i & (1 << v) != 0 or adj[u][v] == 0:
                continue
            # add number of ways to color v
            dp[v][i | (1 << v)] += dp[u][i]
            dp[v][i | (1 << v)] %= MOD

# sum up all the possible colorings
ans = 0
for i in range(1, 2 ** n):
    ans += dp[n - 1][i]
    ans %= MOD

stdout.write(str(ans))
