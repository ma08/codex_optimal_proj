

# solution:
# python3

import sys
import threading

class TreeHeight:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.depth = [0] * self.n

    def compute_height(self, vertex):
        if self.depth[vertex] != 0:
            return self.depth[vertex]
        if self.parent[vertex] == -1:
            self.depth[vertex] = 1
        else:
            self.depth[vertex] = self.compute_height(self.parent[vertex]) + 1
        return self.depth[vertex]

    def compute_height_iterative(self):
        for vertex in range(self.n): self.compute_height(vertex)
        return max(self.depth) + 1


def main():
    tree = TreeHeight()
    print(tree.compute_height_iterative())

threading.Thread(target = main).start()
