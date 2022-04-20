
# Read input
n, m, d = map(int, input().split())  # n is number of nodes, m is number of edges, d is distance from 1 to d
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Check if possible
possible = False
for i in range(m):  # check if node 1 has an edge
    if edges[i][0] == 1:
        possible = True
        break

if not possible:
    print("NO")
    exit()

# Build graph
graph = {}
for i in range(1, n+1):  # initialize graph
    graph[i] = []
for edge in edges:  # add edges to graph
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# Find spanning tree (breadth first search)
tree = []
visited = [False for _ in range(n+1)]
queue = [1, None]
visited[1] = True
while len(queue) > 0:  # while queue is not empty
    node = queue.pop(0)
    if node is not None:  # if node is not None
        for neighbor in graph[node]:
            if not visited[neighbor]:  # if neighbor has not been visited
                tree.append((node, neighbor))  # add edge to tree
                visited[neighbor] = True  # mark neighbor as visited
                queue.append(neighbor)  # add neighbor to queue
                queue.append(None)  # add None to queue
                break  # break out of for loop

# Check if tree is valid
d1 = 0  # number of edges from 1 to d
for edge in tree:
    if edge[0] == 1 or edge[1] == 1:
        d1 += 1
if d1 != d:  # if number of edges from 1 to d is not equal to d
    print("NO")
    exit()

# Print tree (YES followed by edges)
print("YES")
for edge in tree:
    print(edge[0], edge[1])
