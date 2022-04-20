

import sys

sys.setrecursionlimit(10 ** 7)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())

INF = 10 ** 18


def dfs(v, p, g, visited):
    visited[v] = True
    for u in g[v]:
        if u != p:
            dfs(u, v, g, visited)


def solve(n, m, edges):
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    visited = [False] * (n + 1)
    dfs(1, 0, g, visited)
    for v in visited:
        if not v:
            return 'NO'

    # 全ての辺が互いに連結であることが分かっている
    # ある頂点から出る辺を全て逆向きにすれば、その頂点とその頂点への辺を除いた部分グラフは木となる
    # 木は最長パスが2であることが分かっているので、そのようにすればよい
    # ただし、そのままだと、頂点から出る辺が1本の場合について、その辺を逆向きにすると頂点は孤立してしまう
    # そのため、頂点から出る辺が1本の場合はその辺を逆向きにしないようにする
    res = [0] * m
    for i, (u, v) in enumerate(edges):
        if len(g[u]) == 1:
            res[i] = 1

    return 'YES\n' + ''.join(map(str, res))


if __name__ == '__main__':
    n, m = read_list_int()
    edges = [read_list_int() for _ in range(m)]

    print(solve(n, m, edges))