import math
from heapq import heappush, heappop
from collections import defaultdict
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
a = []
for _ in range(n):
    a.append(stdin.readline().strip())

edges = defaultdict(list)
for i in range(n):
    for j in range(m):
        if a[i][j] == '#':
            continue
        if i > 0 and a[i-1][j] != '#':
            edges[(i, j)].append((i-1, j))
        if i < n-1 and a[i+1][j] != '#':
            edges[(i, j)].append((i+1, j))
        if j > 0 and a[i][j-1] != '#':
            edges[(i, j)].append((i, j-1))
        if j < m-1 and a[i][j+1] != '#':
            edges[(i, j)].append((i, j+1))

start = None
end = None
for i in range(n):
    for j in range(m):
        if a[i][j] == 'A':
            start = (i, j)
        if a[i][j] == 'B':
            end = (i, j)

def dijkstra(start, end):
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        d, u = heappop(queue)
        if dist[u] < d:
            continue
        if u == end:
            return d
        for v in edges[u]:
            alt = d + 1
            if alt < dist[v]:
                dist[v] = alt
                heappush(queue, (alt, v))

    return -1

stdout.write(str(dijkstra(start, end)) + '\n')
