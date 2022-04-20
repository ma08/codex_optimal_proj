

# Read input
n, m, d = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

# Check if possible
possible = False
for i in range(m):
    if edges[i][0] == 1 or edges[i][1] == 1:
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

# Find spanning tree with d edges from 1
def find_tree(tree, visited, graph, d):
    if len(tree) == d:
        return True
    for neighbor in graph[1]:
        if not visited[neighbor]:
            tree.append((1, neighbor))
            visited[neighbor] = True
            if find_tree(tree, visited, graph, d):
                return True
            tree.pop()
            visited[neighbor] = False
    return False

visited = [False for _ in range(n+1)] 
tree = [] 
visited[1] = True 
if not find_tree(tree, visited, graph, d):
    print("NO")
    exit()

# Print tree
print("YES")
for edge in tree:
    print(edge[0], edge[1])
