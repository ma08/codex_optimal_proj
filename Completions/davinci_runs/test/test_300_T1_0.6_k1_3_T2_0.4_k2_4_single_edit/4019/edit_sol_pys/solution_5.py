
from collections import deque

if __name__ == "__main__":
    n, m, d = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        v, u = map(int, input().split())
        g[v - 1].append(u - 1)
        g[u - 1].append(v - 1)

    q = deque([0])
    used = [False] * n
    used[0] = True
    ans = []

    while q:
        v = q.popleft()
        for u in g[v]:
            if not used[u]:
                used[u] = True
                ans.append((v, u))
                q.append(u)

    if len(ans) < n - 1:
        print("NO")
    else:
        print("YES")
        if d == 0:
            for v, u in ans:
                print(v + 1, u + 1)
        else:
            for v, u in ans[:-1]:
                print(v + 1, u + 1)
            print(ans[-1][0] + 1, ans[-1][1] + 1)
            print(1, ans[-1][0] + 1)
            for i in range(d - 2):
                print(1, ans[i][1] + 1)
