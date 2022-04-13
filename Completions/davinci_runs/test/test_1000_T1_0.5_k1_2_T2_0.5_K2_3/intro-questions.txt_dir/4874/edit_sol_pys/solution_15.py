
N, M = map(int, input().split())  # N rows and M columns
grid = [input() for _ in range(N)]

count = 0

for i in range(N):  # first row
    for j in range(M):
        if grid[i][j] == '_':  # if there is a space
            count += 1
print(count)
