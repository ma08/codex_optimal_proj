
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
queue = deque()
queue.append(1)
visited[1] = True
count = 0

l = [[] for i in range(N)]
for i in range(M):
    l[city[i][0] - 1].append(city[i][1])

for i in range(N):
    l[i].sort()

for i in range(M):
    print("%06d%06d" % (city[i][0], l[city[i][0] - 1].index(city[i][1]) + 1))
