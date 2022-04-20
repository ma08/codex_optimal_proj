
import sys
import heapq
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
input = sys.stdin.readline


def dfs(v, d, c):
    for i in range(len(G[v])):
        if d[G[v][i]] != -1:
            continue
        d[G[v][i]] = d[v] + 1
        c[G[v][i]] = c[v] + 1 if v != 0 else 0
        dfs(G[v][i], d, c)


def bfs(s):
    q = deque([s])
    d = [-1] * N
    d[s] = 0
    c = [0] * N
    while q:
        v = q.popleft()
        for i in range(len(G[v])):
            if d[G[v][i]] != -1:
                continue
            d[G[v][i]] = d[v] + 1
            c[G[v][i]] = c[v] + 1 if v != 0 else 0
            q.append(G[v][i])
    return d, c


def main(L, R):
    d, c = bfs(0)
    print(d)
    print(c)
    return


if __name__ == "__main__":
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    main()
