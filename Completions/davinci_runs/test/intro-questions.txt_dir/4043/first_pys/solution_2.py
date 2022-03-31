
import sys, heapq, math
from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.children = []

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    xRoot = find(x)
    yRoot = find(y)
    if xRoot != yRoot:
        if len(xRoot.children) > len(yRoot.children):
            xRoot.children.append(yRoot)
            yRoot.parent = xRoot
        else:
            yRoot.children.append(xRoot)
            xRoot.parent = yRoot
    return xRoot

def dfs(root, edges, k):
    if len(root.children) == 0:
        return
    if len(edges) == 0:
        print("NO")
        sys.exit()
    root_num = root.value
    if len(root.children) < k:
        edges = sorted(edges)
        for i in range(k - len(root.children)):
            if edges[i][0] == root.value or edges[i][1] == root.value:
                print("NO")
                sys.exit()
            root.children.append(union(nodes[edges[i][0]], nodes[edges[i][1]]))
        edges = edges[k - len(root.children):]
    for child in root.children:
        dfs(child, edges, k)

n, d, k = list(map(int, input().split()))
nodes = [Node(i) for i in range(1, n + 1)]
edges = defaultdict(list)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        weight = math.sqrt((i - j) ** 2)
        edges[weight].append((i, j))

if d > math.sqrt(n) or k >= n:
    print("NO")
    sys.exit()

# make a spanning tree
edges = sorted(edges)
for i in range(n - 1):
    if edges[i][0] == 1 or edges[i][1] == 1:
        print("NO")
        sys.exit()
    union(nodes[edges[i][0]], nodes[edges[i][1]])
edges = edges[n - 1:]

# dfs
dfs(nodes[1], edges, k)

# print the edges
print("YES")
for i in range(2, n + 1):
    print(find(nodes[i]).value, i)