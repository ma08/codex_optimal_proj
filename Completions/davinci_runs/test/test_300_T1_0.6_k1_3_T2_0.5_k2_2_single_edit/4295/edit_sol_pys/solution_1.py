import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in adj[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

def main():
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    dfs(1)
    print(visited)

if __name__ == '__main__':
    main()
