

import math
import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
    for i in range(N):
        if i == N-1:
            if A[i] == x:
                return True
            else:
                return False
        if A[i] >= x:
            continue
        if A[i] + K < x:
            return False
        if A[i+1] - K > x:
            return False
    return True


visited = set()
dfs(0, visited)

if len(visited) != N:
    print(0)
    sys.exit()

ans = 1
for i in range(N):
    if i == 0:
        continue
    if len(tree[i]) > 1:
        ans *= len(tree[i])

print(ans)
