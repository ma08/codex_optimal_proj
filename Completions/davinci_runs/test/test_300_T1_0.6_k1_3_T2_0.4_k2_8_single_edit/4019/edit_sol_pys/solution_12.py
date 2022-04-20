

from collections import deque

if __name__ == "__main__":
    n, d = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[i].append(i + 1)
        g[i + 1].append(i)

    q = deque([1])
    used = [False] * n
    used[1] = True
    ans = []

    while q:
        v = q.popleft()
        for u in g[v]:
            if not used[u]:
                used[u] = True
                ans.append((v, u))
                q.append(u)


    if d == 0:
        for v, u in ans:
            print(v, u)
    else: 
        for v, u in ans[:-1]:
            print(v, u)
        print(ans[-1][0], ans[-1][1])
        print(1, ans[-1][0])
        for i in range(d - 2):
            print(1, ans[i][1])
