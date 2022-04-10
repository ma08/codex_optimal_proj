

# SOLUTION
# This problem can be solved by using a bipartite graph, where the
# vertices on the left correspond to the squares of the board, and
# the vertices on the right correspond to the tiles.
#
# There is an edge between a square and a tile if the tile can be
# placed on the square. We can check this by comparing the values
# of the tile with the values of the squares on the left and right.
#
# We can then find the maximum matching of the graph using the
# Hopcroft-Karp algorithm, which runs in O(E sqrt(V)), or
# O(n^3 * m^3) in our case.
#
# If the maximum matching is equal to the number of squares, then
# there is a way to place the tiles, otherwise there is not.

import sys
import heapq
from collections import deque

sys.setrecursionlimit(10000)

def hopcroftKarp(graph, n, m):
    """
    Finds the maximum matching of a bipartite graph using the
    Hopcroft-Karp algorithm.
    """
    match = [-1] * n
    dist = [-1] * n
    queue = deque()

    def bfs():
        """
        Performs a breadth-first search to find the shortest path
        to an unmatched vertex.
        """
        for i in range(n):
            if match[i] == -1:
                dist[i] = 0
                queue.append(i)
            else:
                dist[i] = -1

        dist[-1] = -1
        while queue:
            u = queue.popleft()
            if u != -1:
                for v in graph[u]:
                    if dist[match[v]] == -1:
                        dist[match[v]] = dist[u] + 1
                        queue.append(match[v])

        return dist[-1] != -1

    def dfs(u):
        """
        Performs a depth-first search to find an augmenting path.
        """
        if u != -1:
            for v in graph[u]:
                if dist[match[v]] == dist[u] + 1 and dfs(match[v]):
                    match[v] = u
                    match[u] = v
                    return True
            dist[u] = -1
            return False
        return True

    matching = 0
    while bfs():
        for i in range(n):
            if match[i] == -1 and dfs(i):
                matching += 1

    return matching

def solve(n, m):
    """
    Returns whether it is possible to place the tiles in the board
    such that the board is symmetric.
    """
    board = [[0] * (m + 1) for _ in range(m + 1)]
    tiles = [[0] * 4 for _ in range(n)]

    for i in range(n):
        for j in range(4):
            tiles[i][j] = int(input())

    for i in range(1, m + 1):
        for j in range(1, m + 1):
            board[i][j] = int(input())

    graph = [[] for _ in range(m * m + n)]

    # Add edges between each square and each tile that can be placed
    # on that square.
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            for k in range(n):
                if (board[i][j] == tiles[k][0] and board[i][m - j + 1] == tiles[k][1] and
                        board[m - i + 1][j] == tiles[k][2] and board[m - i + 1][m - j + 1] == tiles[k][3]):
                    graph[(i - 1) * m + j - 1].append(m * m + k)
                    graph[m * m + k].append((i - 1) * m + j - 1)

    return hopcroftKarp(graph, m * m, n) == m * m

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if solve(n, m):
        print("YES")
    else:
        print("NO")