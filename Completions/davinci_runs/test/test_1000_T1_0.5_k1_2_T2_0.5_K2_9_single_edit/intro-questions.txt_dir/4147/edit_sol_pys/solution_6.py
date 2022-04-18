
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()
def dfs(l, a, b, c, mp):
    if mp >= 0 and (a == A and b == B and c == C):
        return mp
    if mp < 0 or (a > A or b > B or c > C):
        return float('inf')
    ans = float('inf')
    for i in range(len(l)):
        if a < A:
            ans = min(ans, dfs(l, a+l[i], b, c, mp-(A-a)))
        if b < B:
            ans = min(ans, dfs(l, a, b+l[i], c, mp-(B-b)))
        if c < C:
            ans = min(ans, dfs(l, a, b, c+l[i], mp-(C-c)))
        if l[i] >= 2:
            ans = min(ans, dfs(l, a, b, c, mp-1) + 1)
        if i+1 < len(l):
            l[i+1] += l[i]
        ans = min(ans, dfs(l[i+1:], a, b, c, mp-9) + 9)
    return ans
print(dfs(l, 0, 0, 0, 100))
