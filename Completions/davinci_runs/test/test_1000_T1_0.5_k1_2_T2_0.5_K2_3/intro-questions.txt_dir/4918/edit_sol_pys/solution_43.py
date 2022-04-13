
"""
Disjoint set implementation
"""
import sys

"""
    Node class of the disjoint set
    """

"""
        Initialize a node
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self

"""
    Disjoint set class
    """
class DisjointSet:
    """
        Initialize a disjoint set
    """
    def __init__(self):
        """
        Create a set with value val
    """
        self.map = {}

    def make_set(self, val):
    """
        Get the parent node of the value val
        """
        node = Node(val)
        self.map[val] = node

    def find_set(self, val):
        return self.find_set_node(self.map[val])

    def find_set_node(self, node):
    """
        Get the parent node of the node
    """
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.find_set_node(node.parent)
        return node.parent

    """
        Union two sets with value val1 and val2
    """
    def union(self, val1, val2):
        node1 = self.map[val1]
        node2 = self.map[val2]

        parent1 = self.find_set_node(node1)
        parent2 = self.find_set_node(node2)

        if parent1.rank >= parent2.rank:
            parent1.rank = (parent1.rank + 1) if (parent1.rank == parent2.rank) else parent1.rank
            parent2.parent = parent1
        else:
            parent1.parent = parent2


if __name__ == "__main__":
    n, q = [int(x) for x in sys.stdin.readline().split()]
    ds = DisjointSet()
    for i in range(1, n+1):
        ds.make_set(i)

    for _ in range(q):
        line = sys.stdin.readline().split()
        if line[0] == 't':
            ds.union(int(line[1]), int(line[2]))
        else:
            print(ds.find_set(int(line[1])).rank + 1)
