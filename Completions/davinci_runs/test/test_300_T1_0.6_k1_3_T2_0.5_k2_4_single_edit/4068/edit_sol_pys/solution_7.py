
from collections import deque
import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
a = [0 for i in range(n+1)]
b = [0 for i in range(n+1)]
for i in range(m):
    a[i], b[i] = [int(x) for x in sys.stdin.readline().split()]

visited = [False for i in range(n+1)]
edge = [[] for i in range(n+1)]
for i in range(m):
    edge[a[i]].append(b[i])
    edge[b[i]].append(a[i])

# bfs
q = deque()
q.append(1)
visited[1] = True
while len(q) > 0:
    cur = q.popleft()
    for i in edge[cur]:
        if visited[i] == False:
            q.append(i)
            visited[i] = True

for i in visited:
    print(i)

print(visited.count(True))
