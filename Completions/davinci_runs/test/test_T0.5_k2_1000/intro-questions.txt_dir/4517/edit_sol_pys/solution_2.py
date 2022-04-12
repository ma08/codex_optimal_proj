

from collections import defaultdict

def read_data():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    queries = defaultdict(list)
    for _ in range(m):
        k = int(input())
        v = map(int, input().split())
        queries[k].append(v)
    return graph, queries

def dfs(graph, start, end):
    visited = set()
    stack = [(start, 0)]
    while stack:
        node, dist = stack.pop()
        if node == end:
            return dist
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    stack.append((child, dist + 1))

def check_query(graph, queries):
    for query in queries:
        start = query[0]
        for v in query[1:]:
            if dfs(graph, start, v) == 2:
                return True
        return False

def main():
    graph, queries = read_data()
    for k in queries:
        if check_query(graph, queries[k]):
            print("YES") 
        print("NO")

if __name__ == "__main__":
    main()
