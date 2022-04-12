import sys

def dfs(graph, node, visited, parent):
    visited[node] = True
    for child in graph[node]: 
        if visited[child] == False: 
            if dfs(graph, child, visited, node) == True: 
                return True
        elif parent != child: 
            return True
    return False

def count_cycles(graph):
    visited = [False] * (len(graph) + 1)
    for i in range(1, len(graph) + 1):
        if visited[i] == False:
            if dfs(graph, i, visited, -1) == True:
                return True
    return False

def main():
    n, m = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)

    print('YES' if count_cycles(graph) else 'NO')

if __name__ == '__main__':
    main()
