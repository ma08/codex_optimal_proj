

def get_input():
    """ Gets the input from the user. """
    H, W, K = input().split(" ")
    H, W, K = int(H), int(W), int(K)
    return H, W, K

def get_grid(H, W):
    """ Gets the grid from the user.
    Args:
        H (int): The height of the grid.
        W (int): The width of the grid.
    Returns:
        grid (list): The grid.
    """
    grid = []
    for i in range(H):
        grid.append(input())
    return grid

def count_black(grid, H, W):
    """ Counts the number of black squares in the grid.
    Args:
        grid (list): The grid.
        H (int): The height of the grid.
        W (int): The width of the grid.
    Returns:
        count (int): The number of black squares in the grid.
    """
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                count += 1
    return count

def paint_rows(grid, H, W, rows):
    """ Paints the rows red.
    Args:
        grid (list): The grid.
        H (int): The height of the grid.
        W (int): The width of the grid.
        rows (list): The rows to paint red.
    Returns:
        grid (list): The grid with the rows painted red.
    """
    for i in range(H):
        if i in rows:
            for j in range(W):
                grid[i][j] = "r"
    return grid

def paint_columns(grid, H, W, columns):
    """ Paints the columns red.
    Args:
        grid (list): The grid.
        H (int): The height of the grid.
        W (int): The width of the grid.
        columns (list): The columns to paint red.
    Returns:
        grid (list): The grid with the columns painted red.
    """
    for i in range(H):
        for j in range(W):
            if j in columns:
                grid[i][j] = "r"
    return grid

def count_red(grid, H, W):
    """ Counts the number of red squares.
    Args:
        grid (list): The grid.
        H (int): The height of the grid.
        W (int): The width of the grid.
    Returns:
        count (int): The number of red squares.
    """
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "r":
                count += 1
    return count

def count_choices(grid, H, W, K):
    """ Counts the number of choices that satisfy the condition.
    Args:
        grid (list): The grid.
        H (int): The height of the grid.
        W (int): The width of the grid.
        K (int): The number of black squares.
    Returns:
        count (int): The number of choices that satisfy the condition.
    """
    count = 0
    for i in range(1 << H):
        for j in range(1 << W):
            rows = []
            for k in range(H):
                if i >> k & 1:
                    rows.append(k)
            columns = []
            for k in range(W):
                if j >> k & 1:
                    columns.append(k)
            new_grid = paint_rows(grid, H, W, rows)
            new_grid = paint_columns(new_grid, H, W, columns)
            if count_black(new_grid, H, W) == K and count_red(new_grid, H, W) == H * W - K:
                count += 1
    return count

def main():
    """ The main function. """
    H, W, K = get_input()
    grid = get_grid(H, W)
    choices = count_choices(grid, H, W, K)
    print(choices)

if __name__ == "__main__":
    main()
