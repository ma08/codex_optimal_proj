

import sys

def read_input():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = [int(x) for x in sys.stdin.readline().split()]
        adj[u].append(v)
    return n, adj


def toposort(n, adj):
    in_degree = [0] * (n+1)
    for u in range(1, n+1):
        for v in adj[u]:
            in_degree[v] += 1
    queue = []
    for u in range(1, n+1):
        if in_degree[u] == 0:
            queue.append(u)
    res = []
    while queue:
        u = queue.pop()
        res.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return res


# DFS
def dfs(adj, u):
    visited = [False] * (len(adj))
    stack = [u]
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            for v in adj[u]:
                stack.append(v)
    return visited


def main():
    n, adj = read_input()
    res = toposort(n, adj)
    if len(res) != n:
        print("Sandro fails.")
    else:
        for u in res:
            print(u, end=' ')
        print()

if __name__ == "__main__":
    main()
