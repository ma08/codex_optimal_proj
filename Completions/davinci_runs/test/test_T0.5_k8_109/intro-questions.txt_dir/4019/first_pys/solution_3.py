

import sys
import math

#sys.stdin = open("input.txt", "r")
#sys.stdout = open("output.txt", "w")

n, m, D = map(int, input().split())

if D > n - 1:
    print("NO")
    sys.exit(0)

deg = [0 for i in range(n)]
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])
    deg[a - 1] += 1
    deg[b - 1] += 1

if deg[0] < D:
    print("NO")
    sys.exit(0)

print("YES")

for i in range(m):
    if deg[edges[i][0] - 1] > deg[edges[i][1] - 1]:
        edges[i][0], edges[i][1] = edges[i][1], edges[i][0]

edges.sort(key=lambda x: x[1])

for i in range(n - 1):
    print(edges[i][0], edges[i][1])