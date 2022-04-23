import sys, re
from collections import defaultdict
sys.setrecursionlimit(10**6)

def main():
    N, M = map(int, sys.stdin.readline().split())
    G = defaultdict(set)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        G[a].add(b)
        G[b].add(a)

    visited = [False] * (N + 1)
    def dfs(v):
        visited[v] = True
        for nv in G[v]:
            if not visited[nv]:
                dfs(nv)

    ans = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)

main()
