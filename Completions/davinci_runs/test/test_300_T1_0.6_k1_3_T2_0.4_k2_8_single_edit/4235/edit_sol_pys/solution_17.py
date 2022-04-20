

import sys

def solve(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)

    # DFS
    seen = [False for _ in range(n + 1)]
    def dfs(source):
        seen[source] = True
        for v in graph[source]:
            if not seen[v]:
                dfs(graph, v)

    dfs(1)

    if not all(seen):
        return False

    # find a cycle
    cycle = [False for _ in range(m)]
    seen = [False for _ in range(n + 1)]
    seen[1] = True
    for i in range(m):
        u, v = edges[i]
        if seen[u] and seen[v]:
            cycle[i] = True
        seen[u] = True
        seen[v] = True

    # print(cycle)

    # find a cycle that has at least one even degree node
    def dfs2(source, even_degree_count):
        seen[source] = True
        if len(graph[source]) % 2 == 0:
            even_degree_count += 1
        if len(graph[source]) > 1 and even_degree_count > 1:
            return True
        if len(graph[source]) == 1 and even_degree_count > 0:
            return True
        if len(graph[source]) == 0:
            return even_degree_count > 0
        for v in graph[source]:
            if not seen[v]:
                if dfs2(v, even_degree_count):
                    for u, v in edges:
                        if u == source:
                            cycle[u - 1] = False
                    return True
        return False

    # print(cycle)
    for i in range(m):
        if cycle[i]:
            u, v = edges[i]
            graph[u].remove(v)
            graph[v].remove(u)
            seen = [False for _ in range(n + 1)]
            if dfs2(u, 0):
                cycle[i] = False
            graph[u].append(v)
            graph[v].append(u)

    # print(cycle)
    return cycle


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    edges = [None for _ in range(m)]
    for i in range(m):
        edges[i] = tuple(map(int, sys.stdin.readline().strip().split()))
    cycle = solve(n, m, edges)
    if cycle is False:
        print("NO")
    else:
        print("YES")
        print("".join(map(str, map(int, cycle))))
