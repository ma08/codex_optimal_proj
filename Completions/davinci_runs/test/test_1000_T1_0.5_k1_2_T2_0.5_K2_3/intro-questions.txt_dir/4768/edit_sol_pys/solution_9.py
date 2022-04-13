

def main():
    n, k = map(int, input().split())
    dna = [input() for _ in range(n)]
    mst = kruskal(dna)
    print(mst)
    print(sum(edge.weight for edge in mst))

def kruskal(dna):
    """
    Kruskal's algorithm for finding the minimum spanning tree of a graph.
    """
    # Initialize the graph
    graph = Graph(dna)
    ds = DisjointSets(len(dna))
    # Initialize the minimum spanning tree as an empty list
    mst = []
    # Iterate through the edges in the graph
    for edge in sorted(graph.edges, key=lambda x: x.weight):
        # If the edge does not create a cycle
        if not ds.is_in_same_set(edge.vertex1, edge.vertex2):
            # Add the edge to the minimum spanning tree
            mst.append(edge)
            # Merge the two sets
            ds.union(edge.vertex1, edge.vertex2)
    # Return the minimum spanning tree
    return mst

class Graph:
    """
    Class for representing a graph.
    """
    def __init__(self, dna):
        """
        Initialize the graph.
        """
        self.edges = []
        self.vertices = [i for i in range(len(dna))]
        for vertex1 in range(len(dna)):
            for vertex2 in range(vertex1 + 1, len(dna)):
                self.edges.append(Edge(vertex1, vertex2, self.weight(dna[vertex1], dna[vertex2]), len(dna[vertex1])))
    
    def weight(self, dna1, dna2):
        """
        Compute the weight of an edge between two vertices.
        """
        return sum(1 if dna1[i] != dna2[i] else 0 for i in range(len(dna1))) / len(dna1)

class Edge:
    """
    Class for representing an edge.
    """
    def __init__(self, vertex1, vertex2, weight, length):
        """
        Initialize the edge.
        """
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.length = length

class DisjointSets:
    """
    Class for representing disjoint sets.
    """
    def __init__(self, size):
        """
        Initialize the disjoint set.
        """
        self.size = size
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
    
    def find(self, x):
        """
        Find the root of a given vertex.
        """
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])
    
    def union(self, x, y):
        """
        Merge the sets containing two given vertices.
        """
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        elif self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
    
    def is_in_same_set(self, x, y):
        """
        Check if two given vertices are in the same set.
        """
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    main()
