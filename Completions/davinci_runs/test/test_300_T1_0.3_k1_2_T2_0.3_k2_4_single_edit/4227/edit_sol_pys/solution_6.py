

def dfs(graph, start, visited):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(graph, next, visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = [start]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (N + 1)
    dfs(graph, 1, visited)
    print(visited)
    visited = [False] * (N + 1)
    bfs(graph, 1, visited)
    print(visited)

if __name__ == "__main__":
    main()
