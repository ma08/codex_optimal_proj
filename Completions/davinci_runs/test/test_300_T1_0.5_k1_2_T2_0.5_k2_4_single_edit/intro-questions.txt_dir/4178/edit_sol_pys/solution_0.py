from collections import deque

def bfs(graph, start):
    visited = {}
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited[w] = True
                q.append(w)
    return len(visited)


def main():
    n = int(input())
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    n_components = bfs(graph, 0)
    if n_components == 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
