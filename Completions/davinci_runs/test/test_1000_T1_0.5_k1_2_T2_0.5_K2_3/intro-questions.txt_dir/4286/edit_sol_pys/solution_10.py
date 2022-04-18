
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x - 1].append((y - 1, w))
        g[y - 1].append((x - 1, w))

    spt = [float('inf')] * n
    spt[0] = 0
    q = [0]
    while q:
        u = q.pop(0)
        for v, w in g[u]:
            if spt[v] > spt[u] + w:
                spt[v] = spt[u] + w
                q.append(v)

    ans = sum(a)
    for i in range(1, n):
        ans += min(spt[i], a[i])

    print(ans)


if __name__ == '__main__':
    main()
