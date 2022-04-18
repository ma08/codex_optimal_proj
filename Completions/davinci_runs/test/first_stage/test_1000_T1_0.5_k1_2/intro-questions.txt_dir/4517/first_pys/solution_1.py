

# Solution

import sys
import math
import numpy as np
input = sys.stdin.readline

#input = iter(['10 6', '1 2', '1 3', '1 4', '2 5', '2 6', '3 7', '7 8', '7 9', '9 10', '4 3 8 9 10', '3 2 4 6', '3 2 1 5', '3 4 8 2', '2 6 10', '3 5 4 7']).readline

def read():
    return map(int, input().split())

def read_array(f=int):
    return list(map(f, input().split())) 

def read_matrix(H, W, f=int):
    '''
    Reads an H of lines of space-separated elements of length W,
    and returns a matrix (list of lists) of integers.
    '''
    ret = []
    for _ in range(H):
        ret.append(read_array(f))
    return ret
    
def read_tuple(typ):
    return tuple(map(typ, input().split()))

def read_tuple_array(typ):
    return [read_tuple(typ)]

# If you need to read a single integer, use read()
# If you need to read a space-separated list of integers, use read_array()
# If you need to read a space-separated matrix of integers, use read_matrix()
# If you need to read a space-separated list of integers of unknown length, use read_tuple()
# If you need to read a space-separated list of tuples of integers, use read_tuple_array()

N, M = read()

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.visited = [False] * V
        
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        
    def dfs(self, u):
        self.visited[u] = True
        for v in self.adj[u]:
            if not self.visited[v]:
                self.dfs(v)
    
    def is_connected(self):
        self.dfs(0)
        return all(self.visited)
    
    def is_path(self, u, v):
        self.visited = [False] * self.V
        self.dfs(u)
        return self.visited[v]
    
    def __repr__(self):
        return str(self.adj)

g = Graph(N)

for _ in range(N-1):
    u, v = read()
    g.add_edge(u-1, v-1)

for _ in range(M):
    k = read_array()
    k = k[0]
    nodes = read_array()
    nodes = [n-1 for n in nodes]
    
    #print(nodes)
    if k == 1:
        print("YES")
    else:
        print("YES" if all(g.is_path(nodes[0], n) for n in nodes[1:]) else "NO")