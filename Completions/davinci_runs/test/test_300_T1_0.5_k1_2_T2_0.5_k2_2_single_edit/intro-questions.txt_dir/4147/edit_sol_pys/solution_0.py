

import sys
sys.setrecursionlimit(10**6)

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

l.sort(reverse=True)

def dfs(l, a, b, c, mp, i):
    if mp >= 0 and (a == 0 and b == 0 and c == 0):
        return 0
    if mp < 0 or (a < 0 or b < 0 or c < 0):
        return float('inf')
    ans = float('inf')
    for j in range(i, len(l)):
        if a < A and a+l[j] <= A:
            ans = min(ans, dfs(l, a+l[j], b, c, mp-(A-a-l[j]), j+1))
        if b < B and b+l[j] <= B:
            ans = min(ans, dfs(l, a, b+l[j], c, mp-(B-b-l[j]), j+1))
        if c < C and c+l[j] <= C:
            ans = min(ans, dfs(l, a, b, c+l[j], mp-(C-c-l[j]), j+1))
        if l[i] >= 2:
            ans = min(ans, dfs(l, a, b, c, mp-1, j+1) + 1)
        if j+1 < len(l):
            l[j+1] += l[j]
        ans = min(ans, dfs(l, a, b, c, mp-10, j+1) + 10)
    return ans

print(dfs(l, A, B, C, 100, 0))
