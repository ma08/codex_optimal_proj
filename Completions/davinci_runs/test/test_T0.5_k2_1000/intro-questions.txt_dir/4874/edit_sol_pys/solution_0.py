N, M = map(int, input().split())
grid = [input() for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == '_':
            count += 1
print(count)
