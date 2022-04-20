

N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]

def dfs(n, a, b, c):
    if n == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(n+1, a, b, c)
    ret1 = dfs(n+1, a+l[n], b, c) + 10
    ret2 = dfs(n+1, a, b+l[n], c) + 10
    ret3 = dfs(n+1, a, b, c+l[n]) + 10
    ret4 = dfs(n+1, a+l[n], b+l[n], c) + 20
    ret5 = dfs(n+1, a+l[n], b, c+l[n]) + 20
    ret6 = dfs(n+1, a, b+l[n], c+l[n]) + 20
    return min(ret0, ret1, ret2, ret3, ret4, ret5, ret6)

print(dfs(0, 0, 0, 0))