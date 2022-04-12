

def is_correct(n, grid):
    # check if each row has equal number of black and white squares and no more than two consecutive squares of the same color
    if all(row.count('B') == row.count('W') and 'BBB' not in row and 'WWW' not in row for row in grid):
        # check if each column has equal number of black and white squares and no more than two consecutive squares of the same color
        if all(column.count('B') == column.count('W') and 'BBB' not in column and 'WWW' not in column for column in zip(*grid)):
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    if is_correct(n, grid):
        print(1)
    else:
        print(0)
