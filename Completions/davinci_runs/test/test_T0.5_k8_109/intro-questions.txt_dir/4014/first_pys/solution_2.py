

from collections import defaultdict
from collections import deque

def topological_sort(graph):
    # Kahn's Algorithm
    # https://www.geeksforgeeks.org/topological-sorting/
    # Create a dictionary to store indegrees of all
    # vertices. This dictionary is used to store indegrees
    # of current vertices
    in_degree = {u: 0 for u in graph}
    # Traverse adjacency list to fill indegrees of
    # vertices. This step takes O(V+E) time
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    # Create an queue and enqueue all vertices with
    # indegree 0
    queue = deque()
    for u in in_degree:
        if in_degree[u] == 0:
            queue.appendleft(u)
    # Initialize count of visited vertices
    cnt = 0
    top_order = []
    # One by one dequeue vertices from queue and enqueue
    # adjacents if indegree of adjacent becomes 0
    while queue:
        u = queue.pop()
        top_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            # If in-degree becomes zero, add it to queue
            if in_degree[v] == 0:
                queue.appendleft(v)
        cnt += 1
    # Check if there was a cycle
    if cnt != len(graph):
        return None
    else:
        return top_order

def main():
    n, m = map(int, input().strip().split())
    graph = defaultdict(list)
    for i in range(m):
        s, d, c = map(int, input().strip().split())
        for j in range(s, d):
            graph[j].append(d)
    top_order = topological_sort(graph)
    if top_order is None:
        print(-1)
    else:
        print(top_order)

if __name__ == "__main__":
    main()