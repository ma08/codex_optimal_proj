

def path(graph, a, b, c, i):
    if i == 0:
        return find_path(graph, a, b)
    elif i == 1:
        return find_path(graph, b, c)
    else:
        return find_path(graph, a, c)

def find_path(graph, a, b):
    q = [a-1]
    visited = [False]*len(graph)
    visited[a-1] = True
    while q:
        cur = q.pop(0)
        if cur == b-1:
            return visited
        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    return []

def main():
    n = int(input())
    graph = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        graph[i].sort()
    max_paths = 0
    for i in range(n):
        for j in range(len(graph[i])):
            for k in range(j+1, len(graph[i])):
                a, b, c = i+1, graph[i][j]+1, graph[i][k]+1
                paths = [0]*3
                for l in range(3):
                    paths[l] = len(path(graph, a, b, c, l))
                max_paths = max(max_paths, sum(paths))
                if max_paths == sum(paths):
                    ans = [a, b, c]
    print(max_paths)
    print(*ans)

main()
