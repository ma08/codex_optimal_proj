import sys
from collections import deque
from itertools import permutations


def dfs(start, end):
    stack = deque([start])
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v == end:
                return visited
            stack.extend(graph[v])
    return visited


def main():
    N, M = map(int, input().split())
    graph = dict()
    for i in range(1, N + 1):
        graph[i] = []
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    start, end = map(int, input().split())
    visited = dfs(start, end)
    print(len(visited) - 1)
    if len(visited) > 1:
        print(*visited)


if __name__ == "__main__":
    main()
