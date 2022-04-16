import sys


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []
        self.visited = False

class Graph:
    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n)]
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

    def print_graph(self):
        for n in self.nodes:
            print('id: {}, parent: {}, children: {}'.format(n.id, n.parent.id, [c.id for c in n.children]))

def main():
    n, q = map(int, sys.stdin.readline().split())
    g = Graph(n)
    for i in range(1, n):
        g.add_edge(int(sys.stdin.readline()) - 1, i)
    for _ in range(q):
        u, k = map(int, sys.stdin.readline().split())
        u -= 1
        res = g.dfs(g.nodes[u])
        if k <= len(res):
            print(res[k-1] + 1, flush=True)
        else:
            print(-1)

if __name__ == '__main__':
    main()
