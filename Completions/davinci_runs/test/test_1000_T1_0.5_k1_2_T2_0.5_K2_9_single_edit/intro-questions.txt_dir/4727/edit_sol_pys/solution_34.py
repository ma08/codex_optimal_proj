
# This solution uses the merge function from the previous problem.

def merge(lst):
    if len(lst) <= 1:
        return lst
    else:
        i = 0
        while i < len(lst) - 1:
            if lst[i] == lst[i + 1]:
                lst[i] = lst[i] * 2
                lst.pop(i + 1)
            i += 1
        return lst

def rotate(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append([])
        for row in lst:
            new_lst[i].append(row[i])
    return new_lst

def move_left(grid):
    new_grid = []
    for row in grid:
        new_row = merge([i for i in row if i != 0])
        new_row += [0] * (4 - len(new_row))
        new_grid += [new_row]
    return new_grid

def move_up(grid):
    return move_left(rotate(rotate(rotate(grid))))

def move_right(grid):
    return rotate(rotate(move_left(rotate(rotate(grid)))))

def move_down(grid):
    return rotate(move_left(rotate(rotate(rotate(grid)))))

grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))

direction = int(input())

if direction == 0:
    new_grid = move_left(grid)
elif direction == 1:
    new_grid = move_up(grid)
elif direction == 2:
    new_grid = move_right(grid)
elif direction == 3:
    new_grid = move_down(grid)

for row in new_grid:
    print(*row)
