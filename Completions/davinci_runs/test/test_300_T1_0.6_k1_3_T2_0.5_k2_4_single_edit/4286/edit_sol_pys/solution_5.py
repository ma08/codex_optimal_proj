
import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n+1)]
        self.cost = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        self.is_edge = [[False for _ in range(n+1)] for _ in range(n+1)]

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
        self.cost[u][v] = w
        self.cost[v][u] = w
        self.is_edge[u][v] = True
        self.is_edge[v][u] = True

    def get_minimum_spanning_tree(self):
        visited = [False] * (self.n+1)
        min_heap = []
        heapq.heappush(min_heap, (0, 1))
        total_cost = 0
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
        min_cost = float('inf')
        for i in range(1, self.n+1):
            for j in range(i+1, self.n+1):
                if not self.is_edge[i][j]:
                    min_cost = min(min_cost, self.cost[i][j])
        return total_cost + (self.n - 1) * min_cost - min_cost

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = Graph(n+1)
    for _ in range(m):
        x, y, w = map(int, input().split())
        graph.add_edge(x, y, w)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not graph.is_edge[i][j]:
                graph.add_edge(i, j, a[i] + a[j])
    print(graph.get_minimum_cost())

if __name__ == '__main__':
    main()
