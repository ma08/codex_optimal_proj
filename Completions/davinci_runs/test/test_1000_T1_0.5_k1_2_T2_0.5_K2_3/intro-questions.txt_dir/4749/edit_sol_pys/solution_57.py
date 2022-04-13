

def is_correct(grid):
    n = len(grid)
    # check if each row has an equal number of black and white squares
    for row in grid:
        if row.count('B') != row.count('W'):
            return False
    # check if each column has an equal number of black and white squares
    for i in range(n):
        column = [row[i] for row in grid]
        if column.count('B') != column.count('W'):
            return False
    # check if there are no more than two consecutive squares of the same color
    for row in grid:
        if 'BBB' in row or 'WWW' in row:
            return False
    for i in range(n):
        column = [row[i] for row in grid]
        if 'BBB' in column or 'WWW' in column:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    if is_correct(grid):
        print(1)
    else:
        print(0)
