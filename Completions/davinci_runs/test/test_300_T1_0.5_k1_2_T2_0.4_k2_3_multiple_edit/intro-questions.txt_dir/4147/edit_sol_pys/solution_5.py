
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = [0] * N
for i in range(N):
    l[i] = int(sys.stdin.readline())
l.sort()
def dfs(l, a, b, c, mp, n):
    if n == N:
        if a == A and b == B and c == C:
            return mp
        else:
            return float('inf')
    else:
        if a > A or b > B or c > C:
            return float('inf')
        else:
            ans = float('inf')
            ans = min(ans, dfs(l, a+l[n], b, c, mp-(A-a), n+1))
            ans = min(ans, dfs(l, a, b+l[n], c, mp-(B-b), n+1))
            ans = min(ans, dfs(l, a, b, c+l[n], mp-(C-c), n+1))
            if l[n] >= 2:
                ans = min(ans, dfs(l, a, b, c, mp-1, n+1) + 1)
            ans = min(ans, dfs(l, a, b, c, mp-10, n+1) + 10)
            return ans
print(dfs(l, 0, 0, 0, 100, 0))
