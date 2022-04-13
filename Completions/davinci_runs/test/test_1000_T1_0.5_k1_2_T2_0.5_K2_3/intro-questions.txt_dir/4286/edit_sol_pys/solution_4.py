
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))

    st = [float('inf')] * (n + 1)
    st[1] = 0
    q = [1]
    while q:
        u = q.pop(0)
        for v, w in g[u]:
            if st[v] > st[u] + w:
                st[v] = st[u] + w
                q.append(v)

    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(st[i], a[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
