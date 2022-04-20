

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, s):
        visited = [False] * (len(self.graph))
        stack = []
        stack.append(s)
        visited[s] = True

        while stack:
            s = stack.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True


def BFS(graph, s):
    visited = [False] * (len(graph))
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


def DFS(graph, s):
    visited = [False] * (len(graph))
    stack = []
    stack.append(s)
    visited[s] = True

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for i in graph[s]:
            if visited[i] == False:
                stack.append(i)
                visited[i] = True

import sys

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    graph = defaultdict(list)
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    # print(graph)
    for i in range(k):
        node = int(sys.stdin.readline())
        # BFS(graph, node)
        # DFS(graph, node)
        g = Graph()
        for road in roads:
            g.addEdge(road[0], road[1])
            g.addEdge(road[1], road[0])
        g.BFS(node)
        print("")
        g.DFS(node)
        print("")


if __name__ == "__main__":
    main()
