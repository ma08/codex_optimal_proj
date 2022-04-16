
h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))

# check for rows
for i in range(h):
    all_white = True
    for j in range(w):
        if grid[i][j] == '#':
            all_white = False
            break
    if all_white:
        grid.pop(i)
        h -= 1
        i -= 1

# check for columns
for j in range(w):
    all_white = True
    for i in range(h):
        if grid[i][j] == '#'
            all_white = False
            break
    if all_white:
        for i in range(h):
            grid[i].pop(j)
        w -= 1
        j -= 1

for i in range(h):
    print("".join(grid[i]))
