
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

count = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if grid[i][j] == '_' or grid[i][j] == '|':
            continue
        if grid[i - 1][j] == '|':
            continue
        if grid[i + 1][j] == '|':
            continue
        if grid[i][j - 1] == '_':
            continue
        if grid[i][j + 1] == '_':
            continue
        count += 1
print(count)
