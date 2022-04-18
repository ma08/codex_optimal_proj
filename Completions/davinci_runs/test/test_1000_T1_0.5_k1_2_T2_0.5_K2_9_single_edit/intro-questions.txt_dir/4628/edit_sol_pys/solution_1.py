

def main(n, m, k, edges, routes):
    # compute the minimum spanning tree
    mst = minimum_spanning_tree(edges, n)

    # find the maximum cost edge in the MST
    max_edge = max(mst, key=lambda e: e[-1])

    # zero out the maximum cost edge
    max_edge[-1] = 0

    # compute the shortest paths from the source to each vertex
    dist = dijkstra(mst, n, max_edge[0])

    # compute the total cost of all routes
    route_cost = sum(dist[a-1][b-1] for a, b in routes)

    return route_cost

def minimum_spanning_tree(edges, n):
    # sort the edges by cost
    edges.sort(key=lambda e: e[-1])

    # create a disjoint set of vertices
    ds = DisjointSet(n)

    # create a list to store the edges in the MST
    mst = []

    # for each edge in the sorted list
    for edge in edges:
        # if the vertices are in different sets
        if ds.find(edge[0]-1) != ds.find(edge[1]-1):
            # union the sets
            ds.union(edge[0]-1, edge[1]-1)
            # add the edge to the MST
            mst.append(edge)

    return mst

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank   = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

def dijkstra(edges, n, s):
    # create a list to store the shortest paths to each vertex
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    # create a set to store the vertices
    vertices = set(range(n))

    # set the source distance to 0
    dist[s-1][s-1] = 0

    # while there are vertices to explore
    while vertices:
        # find the vertex with the shortest distance
        v = min(vertices, key=lambda v: dist[s-1][v-1])

        # remove the vertex from the set
        vertices.remove(v)

        # for each edge adjacent to the vertex
        for u, w in edges:
            # if the edge connects the vertex and u
            if v+1 in (u, w):
                # set the distance of u to the distance to v plus the weight of the edge
                dist[s-1][u-1] = min(dist[s-1][u-1], dist[s-1][v-1] + w)
                dist[s-1][w-1] = min(dist[s-1][w-1], dist[s-1][v-1] + w)

    return dist

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    routes = [list(map(int, input().split())) for _ in range(k)]
    print(main(n, m, k, edges, routes))
