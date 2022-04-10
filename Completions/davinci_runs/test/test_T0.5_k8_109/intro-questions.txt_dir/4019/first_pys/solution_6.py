

from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s, degree):
        visited = [False] * self.V
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.popleft()
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    if self.graph[i]:
                        degree += 1
        return degree


if __name__ == "__main__":
    n, m, degree = map(int, input().split())
    g = Graph(n)
    for i in range(m):
        u, v = map(int, input().split())
        g.addEdge(u-1, v-1)
    degree = g.BFS(0, degree)
    if degree == n-1:
        print("YES")
        for i in range(n):
            for j in g.graph[i]:
                if i < j:
                    print(i+1, j+1)
    else:
        print("NO")