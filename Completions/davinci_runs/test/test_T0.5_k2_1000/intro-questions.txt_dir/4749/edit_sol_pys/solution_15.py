
def is_correct(grid):
    n = len(grid)
    # check if rows have equal number of black and white squares
    for row in grid:
        if row.count('B') != row.count('W') or 'BBB' in row or 'WWW' in row:
            return False
    # check if columns have equal number of black and white squares
    for i in range(n):
        column = [row[i] for row in grid]
        if column.count('B') != column.count('W') or 'BBB' in column or 'WWW' in column:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    if is_correct(grid):
        print(1)
    else:
        print(0)
