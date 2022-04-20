

# Read input
n, m, d = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Check if possible
possible = False
for i in range(m):
    if edges[i][0] == 1:
        possible = True
        break

if not possible:
    print("NO")
    exit()

# Build graph
graph = {}
for i in range(1, n+1):
    graph[i] = []
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# Find spanning tree
tree = []
visited = [False for _ in range(n+1)]
queue = [1]
visited[1] = True
while len(queue) > 0:
    node = queue.pop(0)
    if node is not None:
        for neighbor in graph[node]:
            if not visited[neighbor]:
                tree.append((node, neighbor))
                visited[neighbor] = True
                queue.append(neighbor)
                break

# Check if tree is valid
d1 = 0
for edge in tree:
    if edge[0] == 1 or edge[1] == 1:
        d1 += 1
if d1 != d:
    print("NO")
    exit()

# Print tree
print("YES")
for edge in tree:
    print(edge[0], edge[1])
