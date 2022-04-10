

import sys
import collections

class Vertex:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0

class DisjointSet:
    def __init__(self, vertexes):
        self.vertexes = vertexes

    def find(self, v):
        if v.parent != v:
            v.parent = self.find(v.parent)
        return v.parent

    def union(self, v1, v2):
        v1Root = self.find(v1)
        v2Root = self.find(v2)
        if v1Root == v2Root:
            return

        if v1Root.rank < v2Root.rank:
            v1Root.parent = v2Root
        elif v1Root.rank > v2Root.rank:
            v2Root.parent = v1Root
        else:
            v2Root.parent = v1Root
            v1Root.rank += 1

def get_max_diff(n, m, a, segments):
    vertexes = [Vertex(i) for i in range(n)]
    ds = DisjointSet(vertexes)
    graph = collections.defaultdict(list)
    for i in range(m):
        graph[segments[i][0] - 1].append(segments[i][1] - 1)
        graph[segments[i][1] - 1].append(segments[i][0] - 1)
    for i in range(n):
        for j in graph[i]:
            ds.union(vertexes[i], vertexes[j])
    max_diff = 0
    for v in vertexes:
        root = ds.find(v)
        if max_diff < a[v.key] - a[root.key]:
            max_diff = a[v.key] - a[root.key]
    return max_diff

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    segments = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(get_max_diff(n, m, a, segments))

if __name__ == '__main__':
    main()