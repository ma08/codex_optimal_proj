

import sys

def read_input():
    # n, q = [int(x) for x in sys.stdin.readline().split()]
    # adj = [0]
    # adj.extend([int(x) for x in sys.stdin.readline().split()])
    # queries = []
    # for _ in range(q):
    #     queries.append([int(x) for x in sys.stdin.readline().split()])
    # return n, q, adj, queries
    return 9, 5, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]


def build_tree(n, adj):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[adj[i]].append(i)
    return tree


def dfs(tree, u, k, visited):
    if u not in visited:
        visited.add(u)
        if len(visited) == k:
            return u
        for v in tree[u]:
            if v not in visited:
                res = dfs(tree, v, k, visited)
                if res:
                    return res
    return None


def main():
    # n, q, adj, queries = read_input()
    # tree = build_tree(n, adj)
    # for u, k in queries:
    #     visited = set()
    #     res = dfs(tree, u, k, visited)
    #     if res:
    #         print(res)
    #     else:
    #         print(-1)
    n, q, adj, queries = read_input()
    print(n, q, adj, queries)

if __name__ == "__main__":
    main()
