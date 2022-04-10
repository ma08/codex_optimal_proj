import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = input()
ans = 0
def dfs(i, sm):
    global ans
    if i == n:
        if sm == k:
            ans += 1
        return
    if sm > k:
        return
    dfs(i+1, sm)
    dfs(i+1, sm+int(s[i]))
dfs(0, 0)
print(ans)
