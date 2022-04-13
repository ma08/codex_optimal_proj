
n, m = map(int, input().split())

edges = []

for _ in range(m):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: (x[0], x[1]))

def find(x):
    if x == parent[x]: 
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if size[x_root] < size[y_root]:
        x_root, y_root = y_root, x_root
    
    parent[y_root] = x_root
    size[x_root] += size[y_root]

parent = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]

for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])

for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        print(edge[0], edge[1])
