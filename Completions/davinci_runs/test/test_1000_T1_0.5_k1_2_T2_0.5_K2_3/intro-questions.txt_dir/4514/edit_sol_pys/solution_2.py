
import sys

# Read the input
def read_input():
    n, q = [int(x) for x in sys.stdin.readline().split()]
    adj = [0]
    adj.extend([int(x) for x in sys.stdin.readline().split()])
    queries = []
    for _ in range(q):
        queries.append([int(x) for x in sys.stdin.readline().split()])
    return n, q, adj, queries


# Build the tree
def build_tree(n, adj):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[adj[i]].append(i)
    return tree


# BFS
def bfs(tree, u, k, visited):
    if u not in visited:
        visited.add(u)
        if len(visited) == k:
            return u
        for v in tree[u]:
            if v not in visited:
                res = bfs(tree, v, k, visited)
                if res:
                    return res
    return None


def main():
    n, q, adj, queries = read_input()
    tree = build_tree(n, adj)
    for u, k in queries:
        visited = set()
        res = bfs(tree, u, k, visited)
        if res:
            print(res)
        else:
            print(-1)

if __name__ == "__main__":
    main()
