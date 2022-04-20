

import sys


def dfs(v, p):
    for u in g[v]:
        if u != p:
            dfs(u, v)
            cnt[v] += cnt[u]


def dfs2(v, p):
    for u in g[v]:
        if u != p:
            cnt[u] += cnt[v]
            dfs2(u, v)


def dfs3(v, p):
    for u in g[v]:
        if u != p:
            dfs3(u, v)
            cnt[v] += cnt[u]


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    cnt = [0 for _ in range(n)]
    for i in range(n):
        cnt[i] = int(input())
    dfs(0, -1)
    dfs2(0, -1)
    dfs3(0, -1)
    print(*cnt)


if __name__ == "__main__":
    main('dynamic')
