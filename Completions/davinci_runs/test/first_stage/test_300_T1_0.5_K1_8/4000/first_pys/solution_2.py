
import sys
from collections import defaultdict

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

def read_graph(n):
    nodes = [Node(i) for i in range(n)]
    for i in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        a, b = a-1, b-1
        nodes[a].children.append(b)
        nodes[b].children.append(a)
    return nodes

def find_path(nodes, start, end):
    path = []
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == end:
            break
        visited.add(node)
        path.append(node)
        for child in nodes[node].children:
            if child not in visited:
                queue.append(child)
    return path

def find_max_path_size(nodes):
    n = len(nodes)
    max_size = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                path1 = find_path(nodes, i, j)
                path2 = find_path(nodes, j, k)
                path3 = find_path(nodes, i, k)
                path_size = len(set(path1 + path2 + path3))
                max_size = max(max_size, path_size)
    return max_size

def find_max_path_size_optimized(nodes):
    n = len(nodes)
    max_size = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                path1 = find_path(nodes, i, j)
                path2 = find_path(nodes, j, k)
                path3 = find_path(nodes, i, k)
                #path_size = len(set(path1 + path2 + path3))
                path_size = len(set(path1 + path2))
                path_size += len(set(path1 + path3))
                path_size += len(set(path2 + path3))
                path_size -= len(set(path1))
                path_size -= len(set(path2))
                path_size -= len(set(path3))
                path_size += len(set(path1) & set(path2))
                path_size += len(set(path1) & set(path3))
                path_size += len(set(path2) & set(path3))
                path_size += len(set(path1) & set(path2) & set(path3))
                max_size = max(max_size, path_size)
    return max_size

def main():
    n = int(sys.stdin.readline())
    assert 3 <= n <= 200000
    nodes = read_graph(n)
    max_size = find_max_path_size_optimized(nodes)
    print(max_size)

if __name__ == '__main__':
    main()