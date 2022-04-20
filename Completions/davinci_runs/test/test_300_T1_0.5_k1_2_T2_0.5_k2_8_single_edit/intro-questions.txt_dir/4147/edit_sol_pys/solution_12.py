
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

l.sort(reverse=True)

def dfs(l, mp):
    if mp < 0:
        return -1
    if len(l) == 0:
        if A == 0 and B == 0 and C == 0:
            return mp
        else:
            return -1
    ans = float('inf')
    for i in range(4):
        if i == 0:
            nl = l[:]
            if nl[0] >= 2:
                nl[0] -= 2
                nl.sort(reverse=True)
                tmp = dfs(nl, mp-1)
                if tmp != -1:
                    ans = min(ans, tmp+1)
        elif i == 1:
            if A < C:
                nl = l[:]
                nl[0] -= 1
                nl.append(1)
                nl.sort(reverse=True)
                tmp = dfs(nl, mp-(C-A))
                if tmp != -1:
                    ans = min(ans, tmp+(C-A))
        elif i == 2:
            if B < C:
                nl = l[:]
                nl[0] -= 1
                nl.append(1)
                nl.sort(reverse=True)
                tmp = dfs(nl, mp-(C-B))
                if tmp != -1:
                    ans = min(ans, tmp+(C-B))
        else:
            if A < B:
                nl = l[:]
                nl[0] -= 1
                nl.append(1)
                nl.sort(reverse=True)
                tmp = dfs(nl, mp-(B-A))
                if tmp != -1:
                    ans = min(ans, tmp+(B-A))
    return ans

print(dfs(l, 100))
