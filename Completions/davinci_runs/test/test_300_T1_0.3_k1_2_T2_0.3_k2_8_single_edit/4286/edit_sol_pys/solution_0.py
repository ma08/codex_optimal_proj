

def main():
    n, m = map(int, input().split())  # n = number of nodes, m = number of edges
    a = list(map(int, input().split()))  # a = cost of each node

    edges = []  # edges = list of edges
    for _ in range(m):
        x, y, w = map(int, input().split())
        edges.append((w, x, y))

    edges.sort()

    parent = list(range(n))  # parent = parent of each node
    size = [1] * n  # size = size of each node

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            if size[x] < size[y]:
                x, y = y, x
            parent[y] = x
            size[x] += size[y]

    res = 0
    for w, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            res += w
    for i in range(n):
        if find(i) != find(0):
            res += a[i]
            union(i, 0)

    print(res)


if __name__ == '__main__':
    main()
