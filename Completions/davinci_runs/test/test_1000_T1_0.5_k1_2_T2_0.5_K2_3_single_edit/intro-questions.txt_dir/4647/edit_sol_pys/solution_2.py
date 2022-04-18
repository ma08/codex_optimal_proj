

from sys import stdin
from collections import deque

inputLines = deque(stdin.read().splitlines())

# Read the number of vertices
n = int(inputLines.popleft())

# Read the colors of the vertices
colors = list(map(int, inputLines.popleft().split()))

# Read the edges
edges = []
for _ in range(n - 1):
    u, v = map(int, inputLines.popleft().split())
    edges.append((u - 1, v - 1))

# Initialize the adjacency list
adj_list = [[] for _ in range(n)]
for (u, v) in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Initialize the parent array
parent = [-1 for _ in range(n)]

# Initialize the white and black count arrays
white_count = [0 for _ in range(n)]
black_count = [0 for _ in range(n)]

# Initialize the queue
queue = deque()

# Start with the first vertex
queue.append(0)

# Perform BFS
while len(queue) > 0:
    # Get the next vertex
    u = queue.popleft()
    
    # Set the count of the vertex
    white_count[u] = colors[u]
    black_count[u] = 1 - colors[u]
    
    # Visit all the neighbors of the vertex
    for v in adj_list[u]:
        # Skip the parent vertex
        if v == parent[u]:
            continue
        
        # Set the parent of the neighbor
        parent[v] = u
        
        # Add the neighbor to the queue
        queue.append(v)

# Initialize the result array
result = [0 for _ in range(n)]

# Start with the last vertex
queue.append(n - 1)

# Perform BFS
while len(queue) > 0:
    # Get the next vertex
    u = queue.popleft()
    
    # Update the result of the vertex
    result[u] = max(white_count[u] - black_count[u], 0)
    
    # Visit all the neighbors of the vertex
    for v in adj_list[u]:
        # Skip the parent vertex
        if v == parent[u]:
            continue
        
        # Update the white and black counts of the neighbor
        white_count[v] += white_count[u]
        black_count[v] += black_count[u]
        
        # Add the neighbor to the queue
        queue.append(v)

# Print the result
print(' '.join(map(str, result)))
