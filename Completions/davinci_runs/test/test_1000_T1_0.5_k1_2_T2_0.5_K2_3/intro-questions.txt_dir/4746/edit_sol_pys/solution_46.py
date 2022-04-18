

#!/usr/bin/python

from collections import deque

visited = []
graph = []

n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
for i in range(n):
    if not visited[i]:
        queue.append(i)
        visited[i] = True
        while queue:
            curr = queue.popleft()
            for node in graph[curr]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
        print("Connected component: " + str(i))
