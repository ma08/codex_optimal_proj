

# SOLUTION

# Python 3.x
# this solution (TLE) uses the fact that a tree is bipartite

# this function returns the number of vertices in the connected component of a given vertex
def dfs(adj, v, visited):
    visited[v] = True
    count = 1
    for u in adj[v]:
        if not visited[u]:
            count += dfs(adj, u, visited)
    return count

# this function returns the number of connected components of a given graph
def find_components(adj):
    visited = [False] * (n + 1)
    count = 0
    for v in range(1, n + 1):
        if not visited[v]:
            count += 1
            dfs(adj, v, visited)
    return count

n, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# if n - 1 belongs to the interval [2k, 3k], then we can assign each edge to a different company
# if n - 1 belongs to the interval (3k, 4k], then we can assign each edge to a different company
# and make one connected component (with one vertex) a non-good vertex
# if n - 1 belongs to the interval (4k, 5k], then we can assign each edge to a different company
# and make two connected components (with one vertex each) non-good vertices
# and so on...
# if n - 1 belongs to the interval (rk, (r+1)k], then we can assign each edge to a different company
# and make r connected components (with one vertex each) non-good vertices
# the number of companies is r + 1, because one company will have one edge, and the rest of the companies
# will have two edges each

# we find the number of connected components of the graph
components = find_components(adj)

# we find the number of companies
r = (n - 1) // k - components + 1

# we print the number of companies
print(r)

# we print the companies of each edge
for i in range(n - 1):
    print(i % r + 1, end = ' ')