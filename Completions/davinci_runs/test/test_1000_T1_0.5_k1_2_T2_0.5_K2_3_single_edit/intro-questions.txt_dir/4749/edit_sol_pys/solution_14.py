

def is_correct(grid):
    n = len(grid)  # length of grid
    # check if row has equal number of black and white squares
    for row in grid:  # iterate through rows
        if row.count('B') != row.count('W'):  # check if number of black squares is equal to number of white squares
            return False
    # check if column has equal number of black and white squares
    for i in range(n):  # iterate through columns
        column = [row[i] for row in grid]  # get column
        if column.count('B') != column.count('W'):  # check if number of black squares is equal to number of white squares
            return False
    # check if no more than two consecutive squares of the same color
    for row in grid:  # iterate through rows
        if 'BBB' in row or 'WWW' in row:  # check if there are more than two consecutive squares of the same color
            return False
    for i in range(n):  # iterate through columns
        column = [row[i] for row in grid]  # get column
        if 'BBB' in column or 'WWW' in column:  # check if there are more than two consecutive squares of the same color
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    if is_correct(grid):
        print(1)
    else:
        print(0)
