
from collections import defaultdict

def read_data():
    n, m = map(int, input().split()) # n is number of nodes, m is number of queries
    graph = defaultdict(list)
    for _ in range(n - 1): # input edges
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    queries = []
    for _ in range(m): # input queries
        k = int(input())
        v = list(map(int, input().split()))
        queries.append(v)
    return graph, queries

def bfs(graph, start, end): # returns distance between start and end node
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

def check_query(graph, query): # checks if a query is valid
    start = query[0]
    for v in query[1:]: # checks if all nodes are at distance 1 from start node
        if bfs(graph, start, v) == 1:
            return True
    return False

def main():
    graph, queries = read_data()
    for query in queries:
        if check_query(graph, query):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
