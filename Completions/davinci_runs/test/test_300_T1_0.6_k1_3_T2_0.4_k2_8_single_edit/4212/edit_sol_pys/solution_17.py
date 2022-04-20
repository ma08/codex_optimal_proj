

from collections import defaultdict

n, m = map(int, input().split())

# a_i, b_i
pairs = [list(map(int, input().split())) for _ in range(m)]

# graph
graph = defaultdict(set)

for a, b in pairs:
    graph[a].add(b)
    graph[b].add(a)

# dp[i][j] ... maximum score for first i numbers with last number equal j
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if j in graph[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][n])
