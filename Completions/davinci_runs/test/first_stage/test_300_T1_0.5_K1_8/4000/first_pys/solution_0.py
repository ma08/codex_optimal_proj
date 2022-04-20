

import os
import sys

sys.setrecursionlimit(1000000)

def read_ints():
    return list(map(int, input().split()))

def read_int():
    return int(input())

def read_str():
    return input()

def read_strs():
    return list(map(str, input().split()))

def read_str_list():
    return input().split()

def read_grid(rows, read_item):
    return [read_item() for _ in range(rows)]

def read_ints_grid(rows):
    return read_grid(rows, read_int)

def read_strs_grid(rows):
    return read_grid(rows, read_str)

def read_str_list_grid(rows):
    return read_grid(rows, read_str_list)

def read_lines(n, read_item):
    return [read_item() for _ in range(n)]

def read_ints_lines(n):
    return read_lines(n, read_int)

def read_strs_lines(n):
    return read_lines(n, read_str)

def read_str_list_lines(n):
    return read_lines(n, read_str_list)

def write_case_ans(i, ans):
    print("Case #{}: {}".format(i, ans))

def write_line_ans(ans):
    print(ans)

def write_grid(rows):
    for row in rows:
        print(" ".join(map(str, row)))

def write_grid_ans(ans):
    write_grid(ans)

def write_str_list_ans(ans):
    print(" ".join(ans))

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self.edges[a].append(b)
        self.edges[b].append(a)


def read_graph(n, read_edge):
    g = Graph(n)
    for _ in range(n - 1):
        a, b = read_edge()
        g.add_edge(a - 1, b - 1)
    return g

def read_graph_ints(n):
    return read_graph(n, read_ints)

def read_graph_strs(n):
    return read_graph(n, read_strs)

def read_graph_str_list(n):
    return read_graph(n, read_str_list)

def dfs(g, v, p, c):
    c[v] = 1
    for u in g.edges[v]:
        if u == p:
            continue
        dfs(g, u, v, c)

def solve_small(g):
    n = g.n
    c = [0] * n
    dfs(g, 0, -1, c)
    a = c.index(1)
    c = [0] * n
    dfs(g, a, -1, c)
    b = c.index(1)
    c = [0] * n
    dfs(g, b, -1, c)
    c = c.index(1)
    d = [0] * n
    dfs(g, c, -1, d)
    d = d.index(1)
    e = [0] * n
    dfs(g, d, -1, e)
    e = e.index(1)
    f = [0] * n
    dfs(g, e, -1, f)
    f = f.index(1)
    ans = n - 1
    if c in g.edges[d]:
        ans -= 1
    if d in g.edges[e]:
        ans -= 1
    if e in g.edges[f]:
        ans -= 1
    return ans, [a + 1, b + 1, c + 1]

def solve(g):
    n = g.n
    if n <= 10:
        return solve_small(g)
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    ans = n - 1
    if b in g.edges[c]:
        ans -= 1
    if c in g.edges[d]:
        ans -= 1
    if d in g.edges[e]:
        ans -= 1
    if e in g.edges[f]:
        ans -= 1
    return ans, [a + 1, b + 1, c + 1]

def main():
    g = read_graph_ints(read_int())
    ans, abc = solve(g)
    write_line_ans(ans)
    write_str_list_ans(map(str, abc))

if __name__ == "__main__":
    main()