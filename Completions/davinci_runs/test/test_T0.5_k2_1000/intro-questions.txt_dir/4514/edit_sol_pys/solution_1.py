

import sys

def main():
    # Read the input
    n, q = [int(x) for x in input().split()]
    adj = [0] + [int(x) for x in input().split()]
    queries = [tuple(int(x) for x in input().split()) for _ in range(q)]

    # Build the tree
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[adj[i]].append(i)


    for u, k in queries:
        visited = set()
        # DFS to find kth node
        def dfs(u):
            if u not in visited:
                visited.add(u)
                if len(visited) == k:
                    return u
                for v in tree[u]:
                    if v not in visited:
                        res = dfs(v)
                        if res:
                            return res
            return None
        res = dfs(u)
        print(res)



if __name__ == "__main__":
    main()
