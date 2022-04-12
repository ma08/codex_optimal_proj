#!/usr/bin/python3

n = int(input())
grid = []
for i in range(n):
    grid.append(input())

def check_row(row):
    for i in range(n - 2):
        if row[i] == row[i + 1] == row[i + 2]:
            return False
    return True    

def check_column(column):
    for i in range(n - 2):
        if column[i] == column[i + 1] == column[i + 2]:
            return False
    return True    

def check_grid():
    for i in range(n):
        if not check_row(grid[i]):
            return False
        column = []
        for j in range(n):
            column.append(grid[j][i])
        if not check_column(column):
            return False
    return True

if check_grid():
    print(1)
else:
    print(0)
