

def main():
    n, m = map(int, input().split())  # n: 頂点の数, m: 辺の数
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n)]  # グラフの隣接リスト表現
    for edge in edges:
        graph[edge[0]-1].append(edge[1]-1)
        graph[edge[1]-1].append(edge[0]-1)
    print(dfs(graph, n))

def dfs(graph, n):
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
