
#!/usr/bin/env python3

#------------------------------------------------------------------------------#


import sys
import math
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    edges = [0] * (n - 1)
    for i in range(n - 1):
    # n = 2 * 10 ** 5
    # k = 2 * 10 ** 5
    # edges = [0] * (n - 1)
    # for i in range(n - 1):
    #     edges[i] = [i + 1, i + 2]
        edges[i] = list(map(int, sys.stdin.readline().split()))

    print(solve(n, k, edges))

def solve(n, k, edges):
    #
    # Initialization
    #
    parent = [0] * n
    left = [0] * n
    right = [0] * n
    depth = [0] * n
    size = [0] * n

    for i in range(n):
        parent[i] = i
        left[i] = i
        right[i] = i
        depth[i] = 0
        size[i] = 1

    #
    # Construction of the tree
    #
    for i in range(n - 1):
        u, v = edges[i]
        u -= 1
        v -= 1
        parent[v] = u
        left[u] = min(left[u], left[v])
        right[u] = max(right[u], right[v])
        size[u] += size[v]

    #
    # Calculation of the depth
    #
    for i in range(n):
        v = i
        while v != parent[v]:
            depth[v] += 1
            v = parent[v]

    #
    # TODO: Calculate the answer
    #
    ans = 0

    return ans





#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
