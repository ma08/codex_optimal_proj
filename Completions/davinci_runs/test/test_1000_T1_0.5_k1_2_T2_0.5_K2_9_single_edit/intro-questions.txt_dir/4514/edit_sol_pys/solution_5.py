
from collections import deque

class Node:
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        self.children = []
        self.visited = False

    def __str__(self):
        return str(self.id)

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

    def bfs(self, root):
        res = [root.id]
        root.visited = True
        q = deque([root])
        while q:
            curr = q.popleft()
            for c in curr.children:
                if not c.visited:
                    res.append(c.id)
                    c.visited = True
                    q.append(c)
        return res

def main():
    n, q = map(int, input().split())
    g = Graph(n)
    for i in range(1, n):
        g.add_edge(int(input()) - 1, i)
    for _ in range(q):
        u, k = map(int, input().split())
        u -= 1
        res = g.dfs(g.nodes[u])
        if k <= len(res):
            print(res[k-1] + 1)
        else:
            print(-1)

if __name__ == '__main__':
    main()
