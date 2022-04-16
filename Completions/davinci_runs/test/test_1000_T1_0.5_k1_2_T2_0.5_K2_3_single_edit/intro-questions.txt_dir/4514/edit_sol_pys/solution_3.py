

import sys

# Read the input
def read_input():
    n, q = [int(x) for x in sys.stdin.readline().split()]
    adj = [int(x) for x in sys.stdin.readline().split()]
    queries = []
    for _ in range(q):
        queries.append([int(x) for x in sys.stdin.readline().split()])
    return n, q, adj, queries


# Build the tree
def build_tree(n, adj):
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[adj[i]].append(i)
    return tree


# DFS
def dfs(tree, u, k, visited):
    if u not in visited:
        visited.add(u)
        if len(visited) == k-1:
            return u
        for v in tree[u]:
            res = dfs(tree, v, k, visited)
            if res:
                return res
    return None


def main():
    n, q, adj, queries = read_input()
    tree = build_tree(n, adj)
    for u, k in queries:
        visited = set()
        res = dfs(tree, u, k, visited)
        if res:
            print(res)
        else:
            print(-1)

if __name__ == "__main__":
    main()
