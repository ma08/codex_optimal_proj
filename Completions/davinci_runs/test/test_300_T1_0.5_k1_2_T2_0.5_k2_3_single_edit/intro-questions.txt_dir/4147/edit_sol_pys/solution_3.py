
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))


def dfs(l, a, b, c, mp, used):
    if mp >= 0 and (a == A and b == B and c == C):
        return mp
    if mp < 0 or (a > A or b > B or c > C):
        return float('inf')
    ans = float('inf')
    for i in range(N):
        if used[i]:
            continue
        if a < A:
            used[i] = True
            ans = min(ans, dfs(l, a+l[i], b, c, mp-(A-a), used))
            used[i] = False
        if b < B:
            used[i] = True
            ans = min(ans, dfs(l, a, b+l[i], c, mp-(B-b), used))
            used[i] = False
        if c < C:
            used[i] = True
            ans = min(ans, dfs(l, a, b, c+l[i], mp-(C-c), used))
            used[i] = False
        if l[i] >= 2:
            ans = min(ans, dfs(l, a, b, c, mp-1) + 1)
        if i+1 < len(l):
            l[i+1] += l[i]
        ans = min(ans, dfs(l[i+1:], a, b, c, mp-9) + 9)
    return ans

print(dfs(l, 0, 0, 0, 100))
