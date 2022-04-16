
def stars(n, m, grid):
    # print(grid)
    k = 0  # number of stars
    for i in range(n):  # loop through the rows
        for j in range(m):  # loop through the columns
            if grid[i][j] == '*':  # if we find a star
                k += 1  # increment the number of stars
                grid[i][j] = '.'  # remove the star from the grid
                s = 1  # the size of the square
                while i + s < n and i - s >= 0 and j + s < m and j - s >= 0:  # check that we are not out of bounds
                    if grid[i + s][j] == '*' and grid[i - s][j] == '*' and grid[i][j + s] == '*' and grid[i][j - s] == '*':
                        # if the star is in the next row and column
                        grid[i + s][j] = '.'  # remove the star from the grid
                        grid[i - s][j] = '.'  # remove the star from the grid
                        grid[i][j + s] = '.'  # remove the star from the grid
                        grid[i][j - s] = '.'  # remove the star from the grid
                        s += 1  # increment the size of the square
                    else:
                        break  # if the star is not in the next row or column stop
                print(i + 1, j + 1, s - 1)  # print the starting position of the square and its size
    if k == 0:  # if there are no stars
        print(-1)  # print -1
