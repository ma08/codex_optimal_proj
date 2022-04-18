
import sys
from collections import deque



def bfs(graph, n, s):
    d = [-1] * n
    d[s] = 0
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for u in graph[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                q.append(u)
    return d



def solve(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges[1:]:
        graph[u].append(v)
        graph[v].append(u)
    d = bfs(graph, n + 1, 1)
    for i in range(1, n + 1):
        print(d[i], end=' ')


def main():
    reader = (int(x) for x in sys.stdin.readline().split())
    n, m = next(reader), next(reader)
    edges = [None] + [[next(reader), next(reader)] for _ in range(m)]
    solve(n, m, edges)


if __name__ == '__main__':
    main()
