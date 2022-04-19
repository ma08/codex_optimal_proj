import sys
N, A, B, C = map(int, sys.stdin.readline().split())
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

def dfs(l, a, b, c, mp):
    ans = float('inf')
    for i in range(N):
        if a < A:
            ans = min(ans, dfs(l[:i]+l[i+1:], a+l[i], b, c, mp-(A-a)))
        if b < B:
            ans = min(ans, dfs(l[:i]+l[i+1:], a, b+l[i], c, mp-(B-b)))
        if c < C:
            ans = min(ans, dfs(l[:i]+l[i+1:], a, b, c+l[i], mp-(C-c)))
        ans = min(ans, dfs(l[:i]+l[i+1:], a, b, c, mp-10) + 10)
    return ans

print(dfs(l, 0, 0, 0, 100) if dfs(l, 0, 0, 0, 100) < float('inf') else -1)
