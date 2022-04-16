
import math

def solve(n, q, g, queries):
    res = []
    for u, k in queries:
        res.append(dfs(g, u, k))
    return res

def dfs(g, u, k):
    res = [u]
    for c in g[u]:
        res.extend(dfs(g, c, k))
    if k > len(res):
        return -1
    return res[k-1]

def main():
    n, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(1, n):
        g[int(input()) - 1].append(i)
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))
    res = solve(n, q, g, queries)
    for r in res:
        print(r)

if __name__ == '__main__':
    main()

class Node:
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        self.children = []
        self.visited = False

class Graph:
    def __init__(self, n):
        self.nodes = [Node(i, None) for i in range(n)]
        self.nodes[0].parent = self.nodes[0]
        self.nodes[0].visited = True

    def add_edge(self, u, v):
        self.nodes[v].parent = self.nodes[u]
        self.nodes[u].children.append(self.nodes[v])

    def dfs(self, root):
        res = [root.id]
        root.visited = True
        for c in root.children:
            if not c.visited:
                res.extend(self.dfs(c))
        return res
