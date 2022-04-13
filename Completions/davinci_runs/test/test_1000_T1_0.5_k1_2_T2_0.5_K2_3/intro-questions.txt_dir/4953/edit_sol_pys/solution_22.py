

# Program to find the minimum number of vertices to remove from the graph
# to ensure that all remaining vertices are connected

# Define graph class
class Graph:
    # Constructor
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    # Add vertex to the graph
    def add_vertex(self, key):
        # Check if vertex is already in graph
        if key in self.vertices:
            # If key is found, return corresponding vertex object
            return self.vertices[key]
        # Instantiate a new vertex
        new_vertex = Vertex(key)
        # Add new vertex to the vertices dictionary with key
        self.vertices[key] = new_vertex
        # Return the new vertex
        return new_vertex
 
    # Add directed edge from vertex with key `from_key` to vertex with key `to_key`
    def add_directed_edge(self, from_key, to_key):
        # Get the vertex objects corresponding to the from and to keys
        from_vertex = self.add_vertex(from_key)
        to_vertex = self.add_vertex(to_key)
        # Add an edge from the from vertex to the to vertex
        from_vertex.add_edge_to(to_vertex)
 
    # Add an undirected edge between vertex with key `from_key` and vertex with key `to_key`
    def add_undirected_edge(self, from_key, to_key):
        # Add a directed edge from the from key to the to key
        self.add_directed_edge(from_key, to_key)
        # Add a directed edge from the to key to the from key
        self.add_directed_edge(to_key, from_key)
 
    # Return an array of vertex keys in the graph
    def get_vertices(self):
        return self.vertices.keys()
 
    # Get all the neighbor (adjacent-dependencies) of a vertex specified by the vertex key
    def get_neighbors(self, vertex_key):
        # Get the vertex object with the specified vertex_key
        vertex = self.vertices[vertex_key]
        # Return the neighbors of the given vertex object
        return vertex.get_neighbors()
 
    # Return the degree of the vertex specified by the vertex key
    def vertex_degree(self, vertex_key):
        # Get the vertex object with the specified vertex_key
        vertex = self.vertices[vertex_key]
        # Return the degree of the given vertex object
        return vertex.degree()
 
    # Find whether there is a vertex with the given vertex key in the graph or not
    def has_vertex(self, vertex_key):
        # Return True if the vertex key is found in the graph's vertices
        return vertex_key in self.vertices
 
    # Find whether an edge exists between vertices with given `from_key` and `to_key`
    def has_edge(self, from_key, to_key):
        # Get the vertex objects corresponding to the given keys
        from_vertex = self.vertices[from_key]
        to_vertex = self.vertices[to_key]
        # Return True if an edge exists from the from_vertex to the to_vertex
        return from_vertex.has_edge_to(to_vertex)
 
# Define vertex class
class Vertex:
    # Constructor
    def __init__(self, key):
        # Set the key for the vertex
        self.key = key
        # Initialize an empty dictionary for the edges
        self.edges = {}
 
    # Add edge to vertex
    def add_edge_to(self, to_vertex):
        # Set the value of the edge to be the to_vertex
        self.edges[to_vertex.key] = to_vertex
 
    # Get all the neighbor (adjacent-dependencies) of this vertex
    def get_neighbors(self):
        # Return the values of the edges of this vertex object
        return self.edges.values()
 
    # Find whether this vertex has an edge to the vertex with the given key
    def has_edge_to(self, to_vertex_key):
        # Return True if the to_vertex_key is found in the edges of this vertex
        return to_vertex_key in self.edges
 
    # Return the degree of this vertex
    def degree(self):
        # Return the number of edges of this vertex object
        return len(self.edges)
 
# Define function to find the minimum number of vertices to remove from the graph
# to ensure that all remaining vertices are connected
def minimum_vertices_to_remove(graph):
    # Create a set to store the vertices of the graph
    vertices = set(graph.get_vertices())
    # Create a set to store the vertices to be removed
    vertices_to_remove = set()
    # Loop through all vertices in the graph
    for vertex in vertices:
        # Remove the vertex from the graph
        vertices.remove(vertex)
        # Get all the neighbors of the vertex
        neighbors = graph.get_neighbors(vertex)
        # Get all the neighbors of the vertex that are still in the graph
        neighbors_in_graph = set(neighbors).intersection(vertices) # this line is problematic
        # If no neighbors of the vertex are in the graph, add the vertex to the
        # vertices_to_remove set
        if len(neighbors_in_graph) == 0:
            vertices_to_remove.add(vertex)
        # Add the vertex back to the vertices set
        vertices.add(vertex)
    # Return the set of vertices to be removed
    return vertices_to_remove
 
# Create a graph
graph = Graph()
 
# Add an undirected edge between vertex 1 and vertex 2
graph.add_undirected_edge(1, 2)
 
# Add an undirected edge between vertex 1 and vertex 3
graph.add_undirected_edge(1, 3)
 
# Add an undirected edge between vertex 2 and vertex 3
graph.add_undirected_edge(2, 3)
 
# Add an undirected edge between vertex 3 and vertex 4
graph.add_undirected_edge(3, 4)
 
# Add an undirected edge between vertex 4 and vertex 5
graph.add_undirected_edge(4, 5)
 
# Find the minimum number of vertices to remove from the graph
# to ensure that all remaining vertices are connected
vertices_to_remove = minimum_vertices_to_remove(graph)
 
# Print the vertices to be removed
print(vertices_to_remove)
