
n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

def check_row(row):
    color = row[0]
    count = 0
    for i in range(n):
        if row[i] != color:
            color = row[i]
            count = 1
        else:
            count += 1
        else:
            color = row[i]
            count = 1
        if count == 4:
            return False
    return True

def check_column(column):
    color = column[0]
    count = 0
    for i in range(n):
        if column[i] == color:
            count += 1
        else:
            color = column[i]
            count = 1
        if count == 4:
            return False
    return True

def check_grid():
    for i in range(n):
        if not check_row(grid[i]):
            return False
        column = ""
        for j in range(n):
            column += grid[j][i]
        if not check_column(column):
            return False
    return True

if check_grid():
    print(1)
else:
    print(0)
