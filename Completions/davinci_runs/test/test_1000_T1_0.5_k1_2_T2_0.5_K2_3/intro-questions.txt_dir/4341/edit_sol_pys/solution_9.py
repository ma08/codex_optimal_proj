

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
        visited = [False] * (len(self.graph) + 1)
        count = 0
        for i in range(1, len(self.graph) + 1):
            if visited[i] == False:
                if self.isCycle(i, visited, -1) == True:
                    count += 1
        return count
    def cycle_undirected(self):
        visited = [False] * (len(self.graph) + 1) # visited list
        count = 0
        for i in range(1, len(self.graph) + 1):
            if visited[i] == False:
                count += self.isCycle(i, visited, -1)
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
