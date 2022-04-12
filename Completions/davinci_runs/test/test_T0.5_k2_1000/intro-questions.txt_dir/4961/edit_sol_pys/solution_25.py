from collections import deque

def bfs(graph, start, end):
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print(bfs(graph, 'A', 'F'))
