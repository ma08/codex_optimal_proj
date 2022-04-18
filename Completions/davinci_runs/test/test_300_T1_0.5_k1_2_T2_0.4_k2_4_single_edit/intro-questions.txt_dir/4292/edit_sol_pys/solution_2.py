

# import sys

# n, k = [int(i) for i in sys.stdin.readline().split()]
# prices = [int(i) for i in sys.stdin.readline().split()]
# prices.sort()

# print(sum(prices[:k]))


# from collections import deque

# n, k = map(int, input().split())
# a = deque(map(int, input().split()))

# a.rotate(-k)
# print(*a)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v):
#     visited[v] = True
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             dfs(adj[v][i])

# n, m = map(int, sys.stdin.readline().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     adj[a].append(b)
#     adj[b].append(a)

# dfs(1)

# print(visited.count(True)-1)


# from collections import deque

# n, m = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# q = deque()
# q.append(1)
# visited[1] = True

# while q:
#     v = q.popleft()
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             q.append(adj[v][i])
#             visited[adj[v][i]] = True

# print(visited.count(True)-1)


# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v):
#     visited[v] = True
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             dfs(adj[v][i])

# n, m = map(int, sys.stdin.readline().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     adj[a].append(b)
#     adj[b].append(a)

# dfs(1)

# print(visited.count(True)-1)


# from collections import deque

# n, m = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# q = deque()
# q.append(1)
# visited[1] = True

# while q:
#     v = q.popleft()
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             q.append(adj[v][i])
#             visited[adj[v][i]] = True

# print(visited.count(True)-1)


# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v):
#     visited[v] = True
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             dfs(adj[v][i])

# n, m = map(int, sys.stdin.readline().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     adj[a].append(b)
#     adj[b].append(a)

# dfs(1)

# print(visited.count(True)-1)


# from collections import deque

# n, m = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# q = deque()
# q.append(1)
# visited[1] = True

# while q:
#     v = q.popleft()
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             q.append(adj[v][i])
#             visited[adj[v][i]] = True

# print(visited.count(True)-1)


# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v):
#     visited[v] = True
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             dfs(adj[v][i])

# n, m = map(int, sys.stdin.readline().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     adj[a].append(b)
#     adj[b].append(a)

# dfs(1)

# print(visited.count(True)-1)


# from collections import deque

# n, m = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# q = deque()
# q.append(1)
# visited[1] = True

# while q:
#     v = q.popleft()
#     for i in range(len(adj[v])):
#         if not visited[adj[v][i]]:
#             q.append(adj[v][i])
