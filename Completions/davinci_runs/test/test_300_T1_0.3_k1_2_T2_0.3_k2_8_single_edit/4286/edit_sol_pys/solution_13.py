

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    edges = []
    for _ in range(M):
        x, y, w = map(int, input().split())
        edges.append((w, x, y))

    edges.sort()

    parent = list(range(N))
    size = [1] * N

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
    for i in range(N):
        if find(i) != find(0):
            res += A[i]
            union(i, 0)

    print(res)


if __name__ == '__main__':
    main()
