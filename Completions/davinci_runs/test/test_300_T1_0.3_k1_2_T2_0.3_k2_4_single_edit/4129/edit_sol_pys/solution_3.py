
import sys

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u-1].append(v-1)
    visited = [False] * n
    queue = [s-1]
    visited[s-1] = True
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    print(sum(1 for v in visited if v))

main()
