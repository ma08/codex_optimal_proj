

def main():
    n, m, s = map(int, input().split())
    graph = {}
    for i in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)

    visited = [0] * (n+1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = 1

    print(n - sum(visited))


main()