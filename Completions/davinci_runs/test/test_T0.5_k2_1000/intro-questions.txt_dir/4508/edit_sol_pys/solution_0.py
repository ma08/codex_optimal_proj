
# solution
# python3

import sys
import threading
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = []
        self.depth = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.depth = [0] * self.n

    def compute_height(self):
        for vertex in range(self.n):
            i = vertex
            while i != -1:
                if self.depth[i] != 0:
                    break
                self.depth[i] = self.depth[self.parent[i]] + 1
                i = self.parent[i]
        return max(self.depth)

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
