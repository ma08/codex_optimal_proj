
#!/usr/bin/env python
import sys
from collections import defaultdict
import re
 
def make_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph
 
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
 
def is_connected(graph):
    return len(bfs(graph, graph.keys()[0])) == len(graph)
 
def is_eulerian(graph):
    return all(len(graph[v]) % 2 == 0 for v in graph)
 
def find_eulerian_tour(graph):
    tour = []
    if is_eulerian(graph):
        tour.append(graph.keys()[0])
        return find_tour(graph, tour[-1], tour)
    else:
        return []
 
def find_tour(graph, v, tour):
    for w in graph[v]:
        if len(graph[w]) == 1:
            tour.append(w)
            del graph[v][graph[v].index(w)]
            del graph[w]
            return find_tour(graph, w, tour)
        elif len(graph[w]) > 1:
            tour.append(w)
            del graph[v][graph[v].index(w)]
            return find_tour(graph, w, tour)
    return tour
 
def main():
    lines = sys.stdin.read().splitlines()
    edges = []
    for line in lines:
        edges.append(re.findall(r'\d+', line))
    graph = make_graph(edges)
    if not is_connected(graph):
        print "Graph is not connected."
    else:
        tour = find_eulerian_tour(graph)
        if len(tour) == 0:
            print "Graph is not Eulerian."
        else:
            print "Tour:", tour
 
if __name__ == "__main__":
    main()
