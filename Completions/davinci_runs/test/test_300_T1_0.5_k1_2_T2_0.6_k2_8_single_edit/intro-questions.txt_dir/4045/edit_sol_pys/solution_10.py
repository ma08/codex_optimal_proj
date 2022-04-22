
import sys
sys.setrecursionlimit(10**8)
def dfs(x, y):
    if x == n:
        return True
    if y == n:
        return False
    if s[x] == t[y]:
        if dfs(x+1, y+1):
            return True
    return dfs(x, y+1)
n = int(input())
s = input()
t = input()

if dfs(0, 0):
    print("YES")
    print("a"*n+"b"*n+"c"*n)
