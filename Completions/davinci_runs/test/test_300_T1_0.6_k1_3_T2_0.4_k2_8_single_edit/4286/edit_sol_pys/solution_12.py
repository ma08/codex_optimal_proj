
import heapq

class Graph:
    def __init__(self, n, m):
        self.n = n + 1
        self.edges = [[] for _ in range(self.n)]
        self.cost = [[float('inf') for _ in range(self.n)] for _ in range(self.n)]
        self.costs = [float('inf')]
        self.is_edge = [[False for _ in range(self.n)] for _ in range(self.n)]
        self.m = m

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
        self.cost[u][v] = w
        self.cost[v][u] = w
        self.is_edge[u][v] = True
        self.is_edge[v][u] = True
        if self.is_edge[u][v]:
            self.costs[u] = min(self.costs[u], w)
            self.costs[v] = min(self.costs[v], w)
        else:
            self.costs[u] = w
            self.costs[v] = w

    def get_minimum_spanning_tree(self):
        visited = [False] * self.n
        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        total_cost = 0.0
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += weight
            for v, w in self.edges[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        return total_cost

    def get_minimum_cost(self):
        total_cost = self.get_minimum_spanning_tree()
        min_cost = min(self.costs)
        return total_cost + (self.n - 2) * min_cost

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = Graph(n, m)
    for _ in range(m):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        graph.add_edge(x, y, w)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not graph.is_edge[i][j]:
                graph.add_edge(i, j, a[i] + a[j])
    print(graph.get_minimum_cost())

if __name__ == '__main__':
    main()
