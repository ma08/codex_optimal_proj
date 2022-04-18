
import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    graph = [[] for i in range(n)]
    for i in range(m): 
        a, b = map(int, sys.stdin.readline().strip().split()) 
        graph[a].append(b)
        graph[b].append(a)
    print(solve(graph))

def solve(graph, routes):
    max_dist = 0
    for r1, r2 in routes:
        d = dijkstra(graph, r1, r2)
        max_dist = max(max_dist, d)
    return max_dist

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in graph[current]:
            distance = distances[current] + graph[current][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append(neighbor)
    return distances[end]

if __name__ == '__main__':
    main()
