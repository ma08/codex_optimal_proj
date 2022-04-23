
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline()))

L.sort()

def dfs(L, a, b, c, mp):
    if mp >= 0 and (a == A and b == B and c == C): return mp
    if mp < 0 or (a > A or b > B or c > C): return float('inf')
    ans = float('inf')
    for i in range(len(L)):
        if a < A: ans = min(ans, dfs(L, a+L[i], b, c, mp-(A-a)))
        if b < B: ans = min(ans, dfs(L, a, b+L[i], c, mp-(B-b)))
        if c < C: ans = min(ans, dfs(L, a, b, c+L[i], mp-(C-c)))
        if L[i] >= 2: ans = min(ans, dfs(L, a, b, c, mp-1) + 1)
        if i+1 < len(L) and L[i] == L[i+1]: L[i+1] += L[i]
        ans = min(ans, dfs(L[i+1:], a, b, c, mp-10) + 10)
        return float('inf')

print(dfs(l, 0, 0, 0, 100))
