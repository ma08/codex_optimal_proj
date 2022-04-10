

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
    def __init__(self, n):
        self.n = n
        self.parent = [0]*n
        self.rank = [1]*n
        self.edge = [0]*n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return False
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.edge[i_id] += self.edge[j_id] + 1
        else:
            self.parent[i_id] = j_id
            self.edge[j_id] += self.edge[i_id] + 1
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        return True

    def get_edges(self, i):
        return self.edge[self.find(i)]


def Is_Tree(edges, n):
    tree = Tree(n)
    for edge in edges:
        if not tree.union(edge[0]-1, edge[1]-1):
            return False
    return tree.get_edges(0) == D


def main():
    global D
    n, m, D = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    if Is_Tree(edges, n):
        print("YES")
        tree = Tree(n)
        for edge in edges:
            if tree.union(edge[0]-1, edge[1]-1):
                print(edge[0], edge[1])
    else:
        print("NO")

threading.Thread(target=main).start()