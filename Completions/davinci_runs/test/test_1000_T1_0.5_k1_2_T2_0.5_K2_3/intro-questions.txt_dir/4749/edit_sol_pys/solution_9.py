

def is_correct(board):
    # check rows
    for row in board:
        if row.count('X') != row.count('O'):
            return False
    # check columns
    for i in range(len(board)):
        column = [row[i] for row in board]
        if column.count('X') != column.count('O'):
            return False
    # check if there are three consecutive X's or O's
    for row in board:
        if 'XXX' in row or 'OOO' in row:
            return False
    for i in range(len(board)):
        column = [row[i] for row in board]
        if 'XXX' in column or 'OOO' in column:
            return False
    return True  # if all tests pass, return True


if __name__ == '__main__':
    n = int(input())
    board = [input() for _ in range(n)]
    if is_correct(board):
        print(1)
    else:
        print(0)
