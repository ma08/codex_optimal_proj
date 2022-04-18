
import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCycle(self, u, visited, parent):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] == False:
                if self.isCycle(v, visited, u) == True:
                    return True
            elif v != parent:
                return True
        return False

    def cycle(self):
        visited = [False] * (len(self.graph))
        count = 0
        for i in range(len(self.graph)):
            if visited[i] == False:
        return count
                if self.isCycle(i, visited, -1) == True:
                    count += 1
    def bfs(self, s):
        visited = [False] * (len(self.graph))
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.popleft()
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return count

def main():
    n, m = [int(x) for x in input().split()]
    g = Graph()
    for i in range(m):
        u, v = [int(x) for x in input().split()]
        g.addEdge(u, v)
    print(g.cycle())

if __name__ == "__main__":
    main()
