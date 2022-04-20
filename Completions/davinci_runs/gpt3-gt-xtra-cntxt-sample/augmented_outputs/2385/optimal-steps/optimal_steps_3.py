
def num_robots_to_place(grid, n, m):
    # Find the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell.
    # This is really a variation of the longest increasing subsequence problem.
    # We can use a dynamic programming approach to solve the problem in O(n * m) time.
    # We will create a grid of zeros and ones where a 1 represents that a robot can be placed in that cell.
    # We will use a 2D array where the first dimension is the row number and the second dimension is the column number.
    robot_grid = [[0 for i in range(m)] for j in range(n)]
    # We will iterate over the rows of the grid.
    for i in range(n):
        # We will iterate over the columns of the grid.
        for j in range(m):
            # We will iterate over the possible robot placements in the previous row.
            # We will start at the first column in the previous row.
            # If we are in the first row then we will start at the first column in the current row.
            for k in range(j + (i == 0), m):
                # If we are in the first row then we will check if the current column is valid for a robot placement.
                # Otherwise we will check if the current column is valid for a robot placement and the previous column is valid for a robot placement.
                if i == 0 and grid[i][j] != grid[i][k] or i > 0 and grid[i][j] != grid[i][k] and robot_grid[i - 1][k]:
                    # If the current column is valid for a robot placement then we will mark it as valid for a robot placement.
                    robot_grid[i][j] = 1
                    break
    # We will initialize the number of robots to place to zero.
    num_robots = 0
    # We will iterate over the rows of the grid.
    for i in range(n):
        # We will iterate over the columns of the grid.
        for j in range(m):
            # If a robot can be placed in the current cell then we will increment the number of robots to place.
            if robot_grid[i][j]:
                num_robots += 1
    # We will return the number of robots to place.
    return num_robots

def max_black_cells(grid, n, m):
    # Find the maximum number of black cells that can be occupied by robots before all movements.
    # We can use a dynamic programming approach to solve the problem in O(n * m) time.
    # We will create a grid of zeros and ones where a 1 represents that a robot can be placed in that cell.
    # We will use a 2D array where the first dimension is the row number and the second dimension is the column number.
    robot_grid = [[0 for i in range(m)] for j in range(n)]
    # We will iterate over the rows of the grid.
    for i in range(n):
        # We will iterate over the columns of the grid.
        for j in range(m):
            # We will iterate over the possible robot placements in the previous row.
            # We will start at the first column in the previous row.
            # If we are in the first row then we will start at the first column in the current row.
            for k in range(j + (i == 0), m):
                # If we are in the first row then we will check if the current column is valid for a robot placement.
                # Otherwise we will check if the current column is valid for a robot placement and the previous column is valid for a robot placement.
                if i == 0 and grid[i][j] != grid[i][k] or i > 0 and grid[i][j] != grid[i][k] and robot_grid[i - 1][k]:
                    # If the current column is valid for a robot placement then we will mark it as valid for a robot placement.
                    robot_grid[i][j] = 1
                    break
    # We will initialize the maximum number of black cells to zero.
    max_black = 0
    # We will iterate over the rows of the grid.
    for i in range(n):
        # We will iterate over the columns of the grid.
        for j in range(m):
            # If a robot can be placed in the current cell and the current cell is black then we will increment the maximum number of black cells.
            if robot_grid[i][j] and grid[i][j] == '0':
                max_black += 1
    # We will return the maximum number of black cells.
    return max_black

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(input())
    for i in range(n):
        grid.append(input())
    print(num_robots_to_place(grid, n, m), max_black_cells(grid, n, m))