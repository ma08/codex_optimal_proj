

def main():
    # Read in the number of vertices and edges
    n, m = map(int, input().split())
    # Initialize the adjacency list
    adj = [[] for _ in range(n)]
    # Loop through each edge
    for _ in range(m):
        # Read in the edge
        a, b = map(int, input().split())
        # Add the edge to the adjacency list
        adj[a].append(b)
        adj[b].append(a)
    # Read in the start and end vertices
    s, t = map(int, input().split())
    # Initialize the queue
    q = []
    # Initialize the visited array
    visited = [False] * n
    # Add the start vertex to the queue
    q.append(s)
    # Set the start vertex as visited
    visited[s] = True
    # Initialize the number of edges
    edges = 0
    # Loop through the queue
    while len(q) > 0:
        # Pop the first vertex
        v = q.pop(0)
        # Loop through each vertex in the adjacency list
        for w in adj[v]:
            # Check if the vertex has been visited
            if not visited[w]:
                # If not, then add it to the queue
                q.append(w)
                # Set it as visited
                visited[w] = True
                # Increment the number of edges
                edges += 1
    # Print the number of edges
    print(edges)

if __name__ == '__main__':
    main()
