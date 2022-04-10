

import sys
import os
import math
from collections import defaultdict
import heapq

sys.setrecursionlimit(1000000)

def readString():
    return sys.stdin.readline().strip()

def readInteger():
    return int(readString())

def readStringSet(n):
    return sys.stdin.readline().split(" ", n)

def readIntegerSet(n):
    return list(map(int, readStringSet(n)))

def readIntegerMatrix(n, m):
    return [readIntegerSet(m) for _ in range(0, n)]

INF = 1000000000

def dfs(v, prev):
    for u in graph[v]:
        if u != prev:
            dfs(u, v)
            subtree[v] += subtree[u]

def dfs2(v, prev, res):
    for u in graph[v]:
        if u != prev:
            dfs2(u, v, res)
            res[0] = max(res[0], subtree[u] * (n - subtree[u]))
            res[1] = max(res[1], subtree[u] * (n - subtree[u]) + res[2])
            res[2] = max(res[2], subtree[u] * (n - subtree[u]))

def solve(n, graph):
    dfs(1, -1)
    res = [0, 0, 0]
    dfs2(1, -1, res)
    return res[1]

if __name__ == "__main__":
    n = readInteger()
    graph = defaultdict(list)
    for i in range(0, n - 1):
        a, b = readIntegerSet(2)
        graph[a].append(b)
        graph[b].append(a)
    subtree = [1] * (n + 1)
    print(solve(n, graph))