# ---- answer -----
import sys
sys.setrecursionlimit(10**9)
n,a,b = map(int, input().split())


def dfs(cur, sum):
    if cur == n:
        if a <= sum <= b:
            return 1
        return 0
    ret = 0
    for i in range(10):
        ret += dfs(cur+1, sum+i)
    return ret

print(dfs(0,0))
