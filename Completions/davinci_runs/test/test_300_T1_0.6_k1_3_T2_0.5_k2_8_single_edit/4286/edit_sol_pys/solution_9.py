
import heapq

class Graph:
    def __init__(self):
        self.edges = []
        self.n = 0

    def add_edge(self, x, y, w):
        self.edges.append((x, y, w))
        self.n = max(self.n, x + 1, y + 1)

    def get_minimum_spanning_tree(self):
        visited = [False] * self.n 
        heap = []
        heapq.heappush(heap, (0, 0))
        total_cost = 0
        while heap:
            w, x = heapq.heappop(heap)
            if visited[x]:
                continue
            visited[x] = True
            total_cost += w
            for y, z in self.edges[x]:
                if not visited[y]:
                    heapq.heappush(heap, (z, y))
        return total_cost

        return self.get_minimum_spanning_tree()

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = Graph(n)
    for _ in range(m):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        graph.add_edge(x, y, w)
    for i in range(n):
        for j in range(n):
            if not graph.is_edge[i][j]:
                graph.add_edge(i, j, a[i] + a[j])
    print(graph.get_minimum_cost())

if __name__ == '__main__':
    main()
