
def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    print(dfs(graph, n))

def dfs(graph, n, m):
    visited = [False for _ in range(n)]
    visited[0] = True
    stack = [0]
    count = 0
    while len(stack) > 0:
        v = stack.pop()
        for i in range(len(graph[v])):
            if not visited[graph[v][i]]:
                visited[graph[v][i]] = True
                stack.append(graph[v][i])
        if len(stack) == 0:
            count += 1
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
                    break
    return count

if __name__ == '__main__':
    main()
