
import heapq

class Graph:
    def __init__(self, n, a):
        self.a = a
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.costs = [float('inf')] * n
        self.is_edge = [[False for _ in range(n)] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
        self.is_edge[u][v] = True
        self.is_edge[v][u] = True
        self.costs[u] = min(self.costs[u], w - a[u] - a[v])
        self.costs[v] = min(self.costs[v], w - a[u] - a[v])

    def get_minimum_spanning_tree(self):
        visited = [False] * self.n
        min_heap = []
        heapq.heappush(min_heap, (0, 0))
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
        return total_cost + sum(self.costs)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = Graph(n, a)
    for _ in range(m):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        graph.add_edge(x, y, w)
    print(graph.get_minimum_cost())

if __name__ == '__main__':
    main()
