

def is_correct(grid):
    n = len(grid)
    # check if row has equal number of black and white squares
    for row in grid:
        if row.count('B') != row.count('W'):
            return False
    # check if column has equal number of black and white squares
    for i in range(n): # i = 0, 1, 2, 3
        column = [row[i] for row in grid] # column = ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']
        if column.count('B') != column.count('W'):
            return False
    # check if no more than two consecutive squares of the same color
    for row in grid:
        if 'BBB' in row or 'WWW' in row:
            return False
    for i in range(n): # i = 0, 1, 2, 3
        column = [row[i] for row in grid] # column = ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']
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
