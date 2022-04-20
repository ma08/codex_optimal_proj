import sys
from collections import deque
sys.setrecursionlimit(10**6)

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (N+1)
    visited[0] = True
    q = deque([0])
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
    print(sum(visited))

if __name__ == '__main__':
    main()
