import sys
sys.setrecursionlimit(10 ** 7)


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def dfs(v, p):
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v)


dfs(0, -1)
