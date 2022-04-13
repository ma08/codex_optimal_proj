
t = int(input())
for i in range(t):
    n = int(input())
    grid = [input() for j in range(n)]

def check_row(row):
    color = row[0]
    count = 0
    for i in range(len(row)):
        if row[i] == color:
            count += 1
        else:
            color = row[i]
            count = 1
        if count == 3:
            return False
    return True

def check_column(column):
    color = column[0]
    count = 0
    for i in range(len(column)):
        if column[i] == color:
            count += 1
        else:
            color = column[i]
            count = 1
        if count == 3:
            return False
    return True

def check_grid():
    for i in range(len(grid)):
        if not check_row(grid[i]):
            return False
        column = ""
        for j in range(len(grid)):
            column += grid[j][i]
        if not check_column(column):
            return False
    return True

if check_grid():
    print(1)
else:
    print(0)
