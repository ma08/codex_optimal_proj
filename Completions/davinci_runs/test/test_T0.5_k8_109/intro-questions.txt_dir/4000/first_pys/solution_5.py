


import sys
import math
import heapq
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations

sys.setrecursionlimit(1000000)

def read_list():
    return [int(x) for x in sys.stdin.readline().strip().split(' ')]

def read_tuple():
    return tuple(read_list())

def read_integer():
    return int(sys.stdin.readline().strip())

graph = defaultdict(set)

def dfs(parent, current, depth):
    graph[current] = depth
    for child in graph[current]:
        if child == parent:
            continue
        dfs(current, child, depth + 1)

def main():
    n = read_integer()
    for i in range(n - 1):
        a, b = read_tuple()
        graph[a].add(b)
        graph[b].add(a)

    dfs(None, 1, 0)

    max_depth = max(graph.values())
    max_vertices = [x[0] for x in graph.items() if x[1] == max_depth]

    # print(max_vertices)

    max_edges = 0
    max_a = max_b = max_c = 0

    for a in max_vertices:
        for b in max_vertices:
            if a == b:
                continue
            for c in max_vertices:
                if a == c or b == c:
                    continue
                edges = graph[a] + graph[b] + graph[c] - 2 * max_depth
                if edges > max_edges:
                    max_a, max_b, max_c = a, b, c
                    max_edges = edges

    print(max_edges)
    print(max_a, max_b, max_c)

if __name__ == '__main__':
    main()