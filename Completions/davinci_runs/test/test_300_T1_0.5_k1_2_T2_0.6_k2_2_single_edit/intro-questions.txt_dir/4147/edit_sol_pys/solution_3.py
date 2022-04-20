
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()


def dfs(l, a, b, c, m):
    if m < 0 or (a > A or b > B or c > C):
        return 1000000000
    if a == A and b == B and c == C:
        return m
    ans = float('inf')
    for i in range(len(l)):
        if a < A and l[i] > 0:
            ans = min(ans, dfs(l, a + l[i], b, c, m - (A - a)))
        if b < B and l[i] > 0:
            ans = min(ans, dfs(l, a, b + l[i], c, m - (B - b)))
        if c < C and l[i] > 0:
            ans = min(ans, dfs(l, a, b, c + l[i], m - (C - c)))
        if l[i] > 2:
            ans = min(ans, dfs(l, a, b, c, m - 1) + 1)
        ans = min(ans, dfs(l[i + 1:], a, b, c, m - 9) + 9)
    return ans


print(dfs(l, 0, 0, 0, 100) - 100)
