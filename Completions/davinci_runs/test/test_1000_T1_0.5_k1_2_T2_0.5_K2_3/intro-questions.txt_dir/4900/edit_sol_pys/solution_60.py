#prims algorithm
import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = []
        self.size = 0

    def add_node(self, node):
        self.nodes.append(node)
        self.size += 1

    def add_edge(self, node1, node2):
        node1.children.append(node2)
        node2.children.append(node1)

    def get_node(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None

    def get_size(self):
        return self.size

    def get_node_at(self, index):
        return self.nodes[index]

    def get_nodes(self):
        return self.nodes

def get_distance(node1, node2):
    return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def print_graph(graph):
    for node in graph.get_nodes():
        print(node.x, node.y, end=" ")
        for child in node.children:
            print(child.x, child.y, end=" ")
        print()

def prims(graph):
    mst = Graph()
    visited = set()
    visited.add(graph.get_node_at(0))
    while len(visited) < graph.get_size():
        min_edge = None
        for node in visited:
            for child in node.children:
                if child not in visited:
                    if min_edge is None:
                        min_edge = (node, child)
                    elif get_distance(node, child) < get_distance(min_edge[0], min_edge[1]):
                        min_edge = (node, child)
        visited.add(min_edge[1])
        mst.add_node(min_edge[0])
        mst.add_node(min_edge[1])
        mst.add_edge(mst.get_node(min_edge[0].x, min_edge[0].y), mst.get_node(min_edge[1].x, min_edge[1].y))
    return mst

def main():
    n = int(input("Enter number of nodes: "))
    graph = Graph()
    for node in range(n):
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        graph.add_node(Node(x, y))
    for i in range(n):
        for j in range(n):
            if j != i:
                graph.add_edge(graph.get_node_at(i), graph.get_node_at(j))
    mst = prims(graph)
    print_graph(mst)

if __name__ == "__main__":
    main()
