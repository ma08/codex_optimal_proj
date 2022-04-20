
import numpy as np
from scipy.sparse.csgraph import dijkstra

N, M = map(int, input().split())
g = np.full((N, N), np.inf)
for i in range(N):
    g[i, i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a - 1, b - 1] = c
    g[b - 1, a - 1] = c

d = dijkstra(g, directed=False)
print(int(d.min()))
