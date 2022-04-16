

N, M = map(int, input().split())
grid = [input() for _ in range(N)]

count = 0
for i in range(M):
    if grid[0][i] == '_':
        count += 1
print(count+1)
