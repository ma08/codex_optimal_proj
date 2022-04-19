

n, a, b, c = map(int, input().split())
ls = [int(input()) for _ in range(n)]

def dfs(cur, aa, bb, cc):
    if aa == a and bb == b and cc == c:
        return 0
    if cur == n:
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, aa, bb, cc))
    res = min(res, dfs(cur + 1, aa + ls[cur], bb, cc) + 10)
    res = min(res, dfs(cur + 1, aa, bb + ls[cur], cc) + 10)
    res = min(res, dfs(cur + 1, aa, bb, cc + ls[cur]) + 10)
    if ls[cur] - 1 > 0:
        res = min(res, dfs(cur + 1, aa + ls[cur] - 1, bb, cc) + 9)
        res = min(res, dfs(cur + 1, aa, bb + ls[cur] - 1, cc) + 9)
        res = min(res, dfs(cur + 1, aa, bb, cc + ls[cur] - 1) + 9)
    if ls[cur] - 2 > 0:
        res = min(res, dfs(cur + 1, aa + ls[cur] - 2, bb, cc) + 8)
        res = min(res, dfs(cur + 1, aa, bb + ls[cur] - 2, cc) + 8)
        res = min(res, dfs(cur + 1, aa, bb, cc + ls[cur] - 2) + 8)
    return res

print(dfs(0, 0, 0, 0))
