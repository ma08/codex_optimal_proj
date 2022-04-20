
import sys

def main():
    # Read data
    n, m, d = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    # Check if there exists a spanning tree with degree d for the first vertex
    if d >= len(adj[0]):
        print("NO")
        return

    # Print the edges of a spanning tree
    print("YES")
    for _ in range(d):
        print("1", adj[0][0] + 1)
        adj[adj[0][0]].remove(0)
        adj[0].remove(adj[0][0])
    for i in range(1, n):
        if adj[i]:
            print(i + 1, adj[i][0] + 1)
            adj[adj[i][0]].remove(i)
            adj[i].remove(adj[i][0])


if __name__ == "__main__":
    main()