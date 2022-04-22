def main():
    n = int(input())
    a = [[] for _ in range(n + 1)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        a[a[i][0]].append(a[i][1])
        a[a[i][1]].append(a[i][0])
    q = [1]
    used = [False] * (n + 1)
    used[1] = True
    while q:
        v = q.pop()
        for u in a[v]:
            if not used[u]:
                used[u] = True
                q.append(u)
    for i in range(1, n + 1):
        if not used[i]:
            print(-1)
            return
    ans = [0] * n
    for i in range(n):
        j = a[i]
        ans[i], ans[j] = ans[j], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
