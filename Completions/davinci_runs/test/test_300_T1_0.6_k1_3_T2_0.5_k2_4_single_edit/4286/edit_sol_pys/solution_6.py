
import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [[] for _ in range(num_vertices)]
        self.cost = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.costs = []
        self.is_edge = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
        self.cost[u][v] = w
        self.cost[v][u] = w
        self.is_edge[u][v] = True
        self.is_edge[v][u] = True
        self.costs.append(w)

    def get_minimum_spanning_tree(self):
        visited = [False] * self.num_vertices
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
        min_cost = min(self.costs)
        return total_cost + (self.num_vertices - 1) * min_cost

def main():
    num_vertices, num_edges = map(int, input().split())
    costs = list(map(int, input().split()))
    graph = Graph(num_vertices)
    for _ in range(num_edges):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        graph.add_edge(x, y, w)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if not graph.is_edge[i][j]:
                graph.add_edge(i, j, costs[i] + costs[j])
    print(graph.get_minimum_cost())

if __name__ == '__main__':
    main()
