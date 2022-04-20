
import sys


def dfs(graph, v, parent, used, color):
    used[v] = True
    for u in graph[v]:
        if u == parent:
            continue
        if used[u]:
            continue
        if dfs(graph, u, v, used, 1 - color):
            return True
    return False


def solve(n, m, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    used = [False] * n
    if dfs(graph, 0, -1, used, 0):
        print('NO')
        return
    color = [None] * n
    for i in range(n):
        if color[i] is None:
            color[i] = 0
            stack = [i]
            while stack:
                v = stack.pop()
                for u in graph[v]:
                    if color[u] is None:
                        color[u] = 1 - color[v]
                        stack.append(u)
    for u, v in edges:
        if color[u - 1] == color[v - 1]:
            print('NO')
            return
    print('YES')
    for u, v in edges:
        if color[u - 1] < color[v - 1]:
            print(0, end='')
        else:
            print(1, end='')


def main():
    reader = (x for x in sys.stdin.readline().split())
    n, m = int(next(reader)), int(next(reader))
    edges = [[int(next(reader)), int(next(reader))] for _ in range(m)]
    solve(n, m, edges)


if __name__ == '__main__':
    main()
