

import sys

def main():
    n, m = map(int, input().split())
    graph = [[False] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True

    def dfs(v, path):
        path.append(v)
        if len(path) == n:
            print(*path)
            sys.exit()
        for i in range(n):
            if graph[v][i] and i not in path:
                dfs(i, path)
        path.pop()

    for i in range(n):
        dfs(i, [])
    print(-1)

main()
