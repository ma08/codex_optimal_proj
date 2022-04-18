

# Get the number of vertices and edges
n, m = map(int, input().split())
# Get the edges
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))
# Initialize a list of lists to store the adjacency lists
adj = [[] for i in range(n)]
# Initialize a list of lists to store the edge weights
w = [[] for i in range(n)]
# Initialize a list to store the visited vertices
visited = [False] * n
# Initialize a list to store the distances to the source vertex
d = [float('inf')] * n
# Initialize a list to store the parents of the vertices
p = [None] * n

# Add the edges to the adjacency lists
for i in range(m):
    adj[edges[i][0] - 1].append(edges[i][1] - 1)
    adj[edges[i][1] - 1].append(edges[i][0] - 1)
    w[edges[i][0] - 1].append(edges[i][2])
    w[edges[i][1] - 1].append(edges[i][2])

# Get the source vertex
source = int(input()) - 1
# Get the destination vertex
dest = int(input()) - 1

# Initialize the source vertex
d[source] = 0

# Run Bellman-Ford's algorithm
for i in range(n - 1):
    # Iterate through the vertices
    for u in range(n):
        # Iterate through the neighbors of the vertex
        for j in range(len(adj[u])):
            # Get the neighbor
            v = adj[u][j]
            # If the vertex has not been visited, then update its distance and parent
            if d[v] > d[u] + w[u][j]:
                d[v] = d[u] + w[u][j]
                p[v] = u

# Print the distance to the destination vertex
print(d[dest])
