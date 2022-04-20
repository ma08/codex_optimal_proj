

def main():
    """
    The main function.
    """
    # Read the input.
    a, n, m = map(int, input().split())
    rain = []
    for _ in range(n):
        rain.append(list(map(int, input().split())))
    umbrellas = []
    for _ in range(m):
        umbrellas.append(list(map(int, input().split())))
    # Run the algorithm.
    answer = solve(a, rain, umbrellas)
    # Print the answer.
    print(answer)

def solve(a, rain, umbrellas):
    """
    The solution function.
    """
    # Sort the umbrellas by weight.
    umbrellas.sort(key=lambda x: x[1])
    # Build the graph.
    graph = build_graph(a, rain, umbrellas)
    # Find the shortest path from 0 to a.
    if not graph.a in graph.shortest_paths(graph.zero):
        return -1
    # Find the answer.
    return graph.shortest_paths(graph.zero)[graph.a]

def build_graph(a, rain, umbrellas):
    """
    Builds the graph.
    """
    # Build the graph.
    graph = Graph()
    # Add the zero node.
    graph.zero = graph.add_node(0)
    # Add the a node.
    graph.a = graph.add_node(a)
    # Add the rain nodes.
    for segment in rain:
        graph.add_node(segment[0])
        graph.add_node(segment[1])
    # Add the umbrella nodes.
    for umbrella in umbrellas:
        graph.add_node(umbrella[0])
    # Add the edges.
    for segment in rain:
        graph.add_edge(segment[0], segment[1], None, 0)
    for umbrella in umbrellas:
        graph.add_edge(graph.zero, umbrella[0], None, 0)
        graph.add_edge(umbrella[0], graph.a, None, umbrella[1])
    # Return the graph.
    return graph

class Graph:
    """
    A simple graph class.
    """
    class Node:
        """
        A simple node class.
        """
        def __init__(self, value):
            self.value = value
            self.edges = []

        def __str__(self):
            return str(self.value)

        def __hash__(self):
            return hash(self.value)

    class Edge:
        """
        A simple edge class.
        """
        def __init__(self, node, weight):
            self.node = node
            self.weight = weight

        def __str__(self):
            return '{0}:{1}'.format(self.node.value, self.weight)

    def __init__(self):
        self.nodes = {}

    def __str__(self):
        result = ''
        for node in self.nodes.values():
            result += '{0} -> ['.format(node)
            for edge in node.edges[:-1]:
                result += '{0}, '.format(edge)
            if node.edges:
                result += '{0}'.format(node.edges[-1])
            result += ']\n'
        return result[:-1]

    def add_node(self, value):
        node = self.Node(value)
        self.nodes[value] = node
        return node

    def add_edge(self, source, target, bidirectional=True, weight=1):
        source = self.nodes[source]
        target = self.nodes[target]
        source.edges.append(self.Edge(target, weight))
        if bidirectional:
            target.edges.append(self.Edge(source, weight))

    def shortest_paths(self, source):
        """
        Finds all shortest paths from the source.
        """
        # Initialize the distance to infinity.
        distances = {}
        for node in self.nodes.values():
            distances[node] = float('inf')
        # Initialize the distance to the source to zero.
        distances[source] = 0
        # Initialize the queue.
        queue = [source]
        # Run the algorithm.
        while queue:
            # Get the next node.
            node = queue.pop(0)
            # Update the distances.
            for edge in node.edges:
                if distances[node] + edge.weight < distances[edge.node]:
                    distances[edge.node] = distances[node] + edge.weight
                    queue.append(edge.node)
        # Return the distances.
        return distances

if __name__ == '__main__':
    main()