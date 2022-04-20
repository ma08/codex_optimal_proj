
import sys
import random
import queue


def read_data():
    n, m, d = [int(x) for x in input().split()]
    edges = []
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        edges.append((u, v))
    return n, m, d, edges


def check_degree(n, m, d, edges):
    """
    return True if a spanning tree with degree of 1 as d exists.
    """
    # Construct the graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    degree_1 = len(graph[1])
    if degree_1 == d:
        return True
    elif degree_1 > d:
        return False

    # BFS
    visited = set()
    visited.add(1)
    q = queue.Queue()
    for v in graph[1]:
        q.put((1, v))
        visited.add(v)

    while not q.empty():
        u, v = q.get()
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                q.put((v, w))
                if len(visited) == n:
                    return True
    return False

def main():
    n, m, d, edges = read_data()
    if check_degree(n, m, d, edges):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
