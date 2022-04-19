

def main():
    n, m = map(int, input().split())  # n: number of vertices, m: number of edges
    a = list(map(int, input().split()))  # a[i]: cost to connect vertex i to vertex 0

    edges = []
    for _ in range(m):
        x, y, w = map(int, input().split())
        edges.append((w, x, y))

    edges.sort()

    parent = list(range(n))
    size = [1] * n

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
