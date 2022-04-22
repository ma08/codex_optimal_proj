import sys
sys.setrecursionlimit(99999999)


def dfs(y, x, color, pre_color, N, M, grid):
    if y < 0 or x < 0 or y >= N or x >= M:
        return
    if grid[y][x] != pre_color:
        return
    if grid[y][x] == color:
        return
    grid[y][x] = color
    dfs(y+1, x, color, pre_color, N, M, grid)
    dfs(y-1, x, color, pre_color, N, M, grid)
    dfs(y, x+1, color, pre_color, N, M, grid)
    dfs(y, x-1, color, pre_color, N, M, grid)


def solve(N, M, grid, Q, query):
    for i in range(Q):
        pre_color = grid[query[i][1] - 1][query[i][0] - 1]
        dfs(query[i][1] - 1, query[i][0] - 1, query[i][2], pre_color, N, M, grid)
    for i in range(N):
        print(' '.join(map(str, grid[i])))



grid = [list(map(int, input().split())) for _ in range(y)]
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
x, y = map(int, input().split())

if y % 2 == 0 and x * 2 <= y and y <= x * 4:
    print('Yes')
else:
    print('No')
