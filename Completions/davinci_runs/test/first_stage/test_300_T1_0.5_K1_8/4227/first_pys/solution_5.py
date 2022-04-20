

import sys
from collections import defaultdict


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(set)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].add(b)
        graph[b].add(a)
    print(dfs(graph, n))


def dfs(graph, n):
    visited = [False] * n
    visited[0] = True
    stack = [1]
    path = 0
    while stack:
        v = stack[-1]
        if len(stack) == n:
            path += 1
            stack.pop()
            visited[v-1] = False
            continue
        for i in graph[v]:
            if not visited[i-1]:
                visited[i-1] = True
                stack.append(i)
                break
        else:
            stack.pop()
            visited[v-1] = False
    return path


if __name__ == "__main__":
    main()