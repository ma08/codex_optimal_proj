

def read_grid():
    return [list(map(int, input().strip().split())) for _ in range(4)]

def write_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def slide_left(row):
    """
    >>> slide_left([2, 0, 0, 2])
    [4, 0, 0, 0]
    >>> slide_left([4, 16, 8, 2])
    [4, 16, 8, 2]
    >>> slide_left([2, 64, 32, 4])
    [2, 64, 32, 4]
    >>> slide_left([1024, 1024, 64, 0])
    [2048, 64, 0, 0]
    >>> slide_left([2, 2, 4, 8])
    [4, 4, 8, 0]
    >>> slide_left([4, 0, 4, 4])
    [8, 4, 0, 0]
    >>> slide_left([16, 16, 16, 16])
    [32, 32, 0, 0]
    >>> slide_left([32, 16, 16, 32])
    [32, 32, 32, 0]
    """
    # slide non-zero tiles to the left
    row = [tile for tile in row if tile]
    # merge tiles
    row = [tile * 2 for i, tile in enumerate(row) if tile == row[i + 1] for i in range(len(row) - 1)] + [tile for i, tile in enumerate(row) if tile != row[i + 1] for i in range(len(row) - 1)]
    # pad with zeros
    row += [0] * (4 - len(row))
    return row

def rotate_90(grid):
    """
    >>> rotate_90([[2, 0, 0, 2], [4, 16, 8, 2], [2, 64, 32, 4], [1024, 1024, 64, 0]])
    [[2, 4, 2, 1024], [0, 16, 64, 1024], [0, 8, 32, 64], [2, 2, 4, 0]]
    >>> rotate_90([[2, 2, 4, 8], [4, 0, 4, 4], [16, 16, 16, 16], [32, 16, 16, 32]])
    [[2, 4, 16, 32], [2, 0, 16, 16], [4, 4, 16, 16], [8, 4, 16, 32]]
    """
    return [[grid[j][i] for j in range(4)] for i in range(3, -1, -1)]

def transpose(grid):
    """
    >>> transpose([[2, 0, 0, 2], [4, 16, 8, 2], [2, 64, 32, 4], [1024, 1024, 64, 0]])
    [[2, 4, 2, 1024], [0, 16, 64, 1024], [0, 8, 32, 64], [2, 2, 4, 0]]
    >>> transpose([[2, 2, 4, 8], [4, 0, 4, 4], [16, 16, 16, 16], [32, 16, 16, 32]])
    [[2, 4, 16, 32], [2, 0, 16, 16], [4, 4, 16, 16], [8, 4, 16, 32]]
    """
    return [[grid[j][i] for j in range(4)] for i in range(4)]

def move_left(grid):
    return [slide_left(row) for row in grid]

def move_right(grid):
    return move_left(rotate_90(rotate_90(grid)))

def move_up(grid):
    return transpose(move_left(transpose(grid)))

def move_down(grid):
    return transpose(move_right(transpose(grid)))

def play(grid, move):
    return {
        0: move_left,
        1: move_up,
        2: move_right,
        3: move_down,
    }[move](grid)

if __name__ == '__main__':
    grid = read_grid()
    move = int(input().strip())
    grid = play(grid, move)
    write_grid(grid)
