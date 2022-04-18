
import sys
from collections import defaultdict
from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(graph, next, visited)

def bfs(graph, start, visited):
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # check if graph is connected
    dfs(graph, 1, visited)
    for i in range(1, n + 1):
        if not visited[i]:
            print("NO\n")
            return

    # check if graph is acyclic
    bfs(graph, 1, visited)
    for i in range(1, n + 1):
        if not visited[i]:
            print("NO\n")
            return

    # if graph is acyclic and connected, then it is a tree
    # therefore, it is possible to orient all edges
    print("YES\n")
    for i in range(1, n + 1):
        for j in graph[i]:
            if i < j:
                print("0", end="")
    for i in range(1, n + 1):
        for j in graph[i]:
            if i > j:
                print("1", end="")

if __name__ == "__main__":
    solve()
