
N, M = map(int, input().split())  # N rows and M columns
grid = [input() for _ in range(N)]

count = 0  # count the spaces in the first row

for i in range(M):  # first row
    if grid[0][i] == '_':  # if there is a space in the first row
        count += 1
print(count)
