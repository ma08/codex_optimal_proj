
from collections import deque
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * n
    queue = deque()
    for i in range(n):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            while queue:
                curr = queue.popleft()
                for node in graph[curr]:
                    if not visited[node]:
                        queue.append(node)
                        visited[node] = True
            print("Connected component: " + str(i))

if __name__ == '__main__':
    main()
