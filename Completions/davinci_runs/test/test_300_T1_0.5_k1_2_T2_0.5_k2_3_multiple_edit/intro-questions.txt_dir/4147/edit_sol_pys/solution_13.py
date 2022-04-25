

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
            ans = min(ans, dfs(l, a+l[i], b, c, mp-(A-a)))  # l[i]をAに加える
        if b < B:
            ans = min(ans, dfs(l, a, b+l[i], c, mp-(B-b)))  # l[i]をBに加える
        if c < C:
            ans = min(ans, dfs(l, a, b, c+l[i], mp-(C-c)))  # l[i]をCに加える
        if i+1 < len(l) and l[i+1] >= 2:  # l[i]とl[i+1]を1にする
            ans = min(ans, dfs(l[:i+1]+[l[i+1]-1], a, b, c, mp-1) + 1)  # l[i]とl[i+1]を1にする
        if i+2 < len(l):
            ans = min(ans, dfs(l[:i+2]+[l[i+1]+l[i+2]], a, b, c, mp-9) + 9)  # l[i]とl[i+1]をl[i+2]にする
    return ans

print(dfs(l, 0, 0, 0, 100))
