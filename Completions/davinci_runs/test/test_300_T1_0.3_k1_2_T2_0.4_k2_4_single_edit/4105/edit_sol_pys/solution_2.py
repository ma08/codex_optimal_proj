
import sys
sys.setrecursionlimit(100000000)
n, k = map(int, input().split())

def print_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(graph[i][j], end=" ")
        print()

def dfs(graph, start, visited):
    visited[start] = True
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and visited[i] == False:
            dfs(graph, i, visited)

def is_connected(graph):
    visited = [False] * len(graph)
    dfs(graph, 0, visited)
    for i in range(len(visited)):
        if visited[i] == False:
            return False
    return True

def is_eulerian(graph):
    if is_connected(graph) == False:
        return False
    odd_count = 0
    for i in range(len(graph)):
        count = 0
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                count += 1
        if count % 2 != 0:
            odd_count += 1
    if odd_count == 0 or odd_count == 2:
        return True
    return False

def has_eulerian_cycle(graph):
    if is_eulerian(graph) == True:
        return True
    return False

def has_eulerian_path(graph):
    if is_eulerian(graph) == True:
        return True
    return False

def find_eulerian_cycle(graph):
    print("YES")
    print_graph(graph)

def find_eulerian_path(graph):
    print("YES")
    print_graph(graph)

def find_cycle(graph):
    if has_eulerian_cycle(graph) == True:
        find_eulerian_cycle(graph)
    elif has_eulerian_path(graph) == True:
        find_eulerian_path(graph)
    else:
        print("NO")

graph = [[0 for i in range(n)] for j in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
find_cycle(graph)
