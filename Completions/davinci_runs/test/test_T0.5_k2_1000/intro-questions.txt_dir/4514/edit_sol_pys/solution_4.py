
import sys

# Read the input
def read_input():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = [int(x) for x in sys.stdin.readline().split()]
        adj[u].append(v)
        adj[v].append(u)
    return n, m, adj


# DFS to find the number of components
def dfs(adj, u, visited):
    if u not in visited:
        visited.add(u)
        for v in adj[u]:
            dfs(adj, v, visited)



# Find the number of components
def find_components(adj):
    visited = set()
    count = 0
    for u in range(1, len(adj)):
        if u not in visited:
            count += 1
            dfs(adj, u, visited)
    return count


def main():
    n, m, adj = read_input()
    print(find_components(adj))

if __name__ == "__main__":
    main()
