

def dfs(idx, lst, cnt):
    if idx == n:
        return cnt
    else:
        return min(dfs(idx+1, lst, cnt), dfs(idx+1, lst, cnt+1))


n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = dfs(0, a, 0)
print(ans)
