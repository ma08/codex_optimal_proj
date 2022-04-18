
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

# read the input and build the graph
n = int(input())
a = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs to find the number of white and black vertices in the sub tree
visited = [False] * (n + 1)
white = defaultdict(int)
black = defaultdict(int)


def dfs(v):
    visited[v] = True
    white[v] = 1 if a[v - 1] == 1 else 0
    black[v] = 1 if a[v - 1] == 0 else 0
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
            white[v] += white[u]
            black[v] += black[u]


dfs(1)

# find the answer
ans = [0] * n
for i in range(1, n + 1):
    for u in graph[i]:
        if visited[u]:
            ans[i - 1] = max(ans[i - 1],
                             abs(white[i] - black[i] - (white[u] - black[u])))
print(*ans)
