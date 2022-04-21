

import sys 
import pprint

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def dfs(start, graph, visited):
    stack = [start]
    visited[start] = True

    while stack:
        vertex = stack.pop()
        for i in graph[vertex]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)


visited = [False] * N

cnt = 0
for i in range(N):
    if not visited[i]:
        dfs(i, graph, visited)
        cnt += 1

print(cnt)
