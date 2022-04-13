
import sys
import heapq

class Graph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.adj_list = [[] for _ in range(num_of_nodes)]
        self.edges = set()

    def add_edge(self, edge):
        # edge = (x, y, weight)
        self.adj_list[edge[0] - 1].append((edge[1] - 1, edge[2]))
        self.adj_list[edge[1] - 1].append((edge[0] - 1, edge[2]))
        self.edges.add((edge[0] - 1, edge[1] - 1))

    def dijkstra(self, start, end):
        visited = [False] * self.num_of_nodes
        dist = [float("inf")] * self.num_of_nodes
        dist[start] = 0

        queue = []
        heapq.heappush(queue, (0, start))
        while queue:
            node = heapq.heappop(queue)
            if visited[node[1]]: continue
            visited[node[1]] = True
            for adj_node in self.adj_list[node[1]]:
                if not visited[adj_node[0]] and dist[adj_node[0]] > dist[node[1]] + adj_node[1]:
                    dist[adj_node[0]] = dist[node[1]] + adj_node[1]
                    heapq.heappush(queue, (dist[adj_node[0]], adj_node[0]))

        return dist[end]

    def kth_shortest_path(self, k):
        dist = []
        for i in range(self.num_of_nodes):
            for j in range(i + 1, self.num_of_nodes):
                if (i, j) not in self.edges:
                    dist.append(self.dijkstra(i, j))
        dist.sort()
        return dist[k - 1]


if __name__ == "__main__":
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, m, k = next(reader)
    graph = Graph(n)
    for edge in reader:
        graph.add_edge(edge)
    print(graph.kth_shortest_path(k))
