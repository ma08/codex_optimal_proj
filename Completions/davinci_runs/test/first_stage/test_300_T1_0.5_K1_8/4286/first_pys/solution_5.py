

import sys


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union_sets(x, y):
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def kruskal(edges, n):
    mst = 0
    for edge in edges:
        x, y, w = edge
        x = find_set(x)
        y = find_set(y)
        if x != y:
            union_sets(x, y)
            mst += w
    if len(set(parent)) == 1:
        return mst
    else:
        return None


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    edges = []
    for _ in range(m):
        x, y, w = [int(x) for x in sys.stdin.readline().split()]
        edges.append((x - 1, y - 1, w))
    edges.sort(key=lambda x: x[2])
    global parent
    parent = [x for x in range(n)]
    global rank
    rank = [0] * n
    mst = kruskal(edges, n)
    if mst is not None:
        print(mst)
    else:
        edges = [(x, y, a[x] + a[y]) for x, y, _ in edges]
        edges.sort(key=lambda x: x[2])
        parent = [x for x in range(n)]
        rank = [0] * n
        print(kruskal(edges, n))


if __name__ == '__main__':
    main()