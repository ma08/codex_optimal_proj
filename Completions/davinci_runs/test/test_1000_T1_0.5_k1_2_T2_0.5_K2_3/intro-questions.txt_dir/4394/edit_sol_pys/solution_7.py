

import sys
from collections import defaultdict
from heapq import heappop, heappush
import heapq

sys.setrecursionlimit(10 ** 6)


def read_list():
    return sys.stdin.readline().strip().split(' ')


def read_single_int():
    return int(sys.stdin.readline().strip())


def read_single_str():
    return sys.stdin.readline().strip()


def read_single_float():
    return float(sys.stdin.readline().strip())


def read_list_int():
    return list(map(int, read_list()))


def read_list_float():
    return list(map(float, read_list()))


class Graph:
    def __init__(self, n, m):
        self.nodes = n
        self.edges = m
        self.graph = defaultdict(list)
        self.weight = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.weight[u].append(w)
        self.weight[v].append(w)

    def find_mst(self):
        self.visited = [False] * self.nodes
        self.visited[0] = True
        self.heap = []
        for v in self.graph[0]:
            heappush(self.heap, (self.find_weight(0, v), 0, v))
        mst = []
        while self.heap:
            w, u, v = heappop(self.heap)
            if not self.visited[v]:
                self.visited[v] = True
                mst.append((u, v, w))
                for to in self.graph[v]:
                    if not self.visited[to]:
                        heappush(self.heap, (self.find_weight(v, to), v, to))
        return mst

    def find_weight(self, u, v):
        return min(self.weight[u] + self.weight[v])

    def find_mst_weight(self, mst):
        return sum([w for u, v, w in mst])

    def find_mst_count(self):
        mst = self.find_mst()
        mst_weight = self.find_mst_weight(mst)
        for i in range(self.edges):
            w = self.weight[i]
            self.weight[i] = w + i
            mst = self.find_mst()
            if mst_weight != self.find_mst_weight(mst):
                self.weight[i] = w
                return i
        return i + 1


def main():
    n, m = read_list_int()
    g = Graph(n, m)
    for i in range(m):
        u, v, w = read_list_int()
        g.add_edge(u - 1, v - 1, w)
    print(g.find_mst_count())


if __name__ == '__main__':
    main()
