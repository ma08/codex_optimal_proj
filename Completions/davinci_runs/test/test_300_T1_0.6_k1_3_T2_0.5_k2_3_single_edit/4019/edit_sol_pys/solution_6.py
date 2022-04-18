
from collections import deque
import sys

if __name__ == "__main__":
    n, m, d = map(int, sys.stdin.readline().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
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
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        if d == 0:
            for v, u in ans:
                sys.stdout.write("{} {}\n".format(v + 1, u + 1))
        else:
            for v, u in ans[:-1]:
                sys.stdout.write("{} {}\n".format(v + 1, u + 1))
            sys.stdout.write("{} {}\n".format(ans[-1][0] + 1, ans[-1][1] + 1))
            sys.stdout.write("{} {}\n".format(1, ans[-1][0] + 1))
            for i in range(d - 2):
                sys.stdout.write("{} {}\n".format(1, ans[i][1] + 1))
