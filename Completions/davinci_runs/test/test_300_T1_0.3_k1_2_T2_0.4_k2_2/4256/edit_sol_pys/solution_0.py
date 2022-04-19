import sys
from collections import deque



def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    print(min(B // A, C))
