h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))

# print("grid: ")
# print(grid)

# check for columns
for i in range(h):
    all_white = True
    for j in range(w):
        if grid[i][j] == '#':
            all_white = False
            break
    if all_white:
        # print("col: " + str(i))
        grid.pop(i)
        h -= 1
        i -= 1

# print("grid: ")
# print(grid)

# check for rows
for j in range(w):
    all_white = True
    for i in range(h):
        if grid[i][j] == '#':
            all_white = False
            break
    if all_white:
        # print("col: " + str(j))
        for i in range(h):
            grid[i].pop(j)
        w -= 1
        j -= 1

# print("grid: ")
# print(grid)

for i in range(h):
    print("".join(grid[i])
