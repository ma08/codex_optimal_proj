
N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c, p):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 * (N - cur)
    ret0 = dfs(cur + 1, a, b, c, 0) + (0 if p == 0 else 10)
    ret1 = dfs(cur + 1, a + ls[cur], b, c, 1) + (0 if p == 1 else 10)
    ret2 = dfs(cur + 1, a, b + ls[cur], c, 2) + (0 if p == 2 else 10)
    ret3 = dfs(cur + 1, a, b, c + ls[cur], 3) + (0 if p == 3 else 10)
    return min(ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0, 0))
