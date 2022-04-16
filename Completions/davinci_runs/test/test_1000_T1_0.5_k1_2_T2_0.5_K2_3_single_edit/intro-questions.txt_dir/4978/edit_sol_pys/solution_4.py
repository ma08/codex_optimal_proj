

import sys, copy

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # each cell is either air, stone, or water
    # water spreads:
    # * if water cell is above air cell, air cell turns into water
    # * if water cell is above stone cell, air cells left or right of water cell turn into water
    # * each second
    # * water stops spreading
    # print grid when water stops spreading
    # assume that all cells outside of the grid behave as air cells
    #   e.g. if water cell is at bottommost row, water will not spread to sides
    #
    # grid is N rows and M columns
    # 2 <= N, M <= 50
    #
    # each of N lines contains a string S of length M
    # S represents one of the rows in the grid
    # S consists of the symbols ".", "#", and "V"
    #   . = air
    #   # = stone
    #   V = water
    
    # spread water
    prev_grid = grid
    new_grid = copy.deepcopy(prev_grid)
    for i in range(N-1, -1, -1):
        for j in range(M):
            if prev_grid[i][j] == 'V':
                if i == N-1:
                    if j == 0:
                        if prev_grid[i-1][j] == '.':
                            new_grid[i-1][j] = 'V'
                        if prev_grid[i-1][j+1] == '.':
                            new_grid[i-1][j+1] = 'V'
                    elif j == M-1:
                        if prev_grid[i-1][j] == '.':
                            new_grid[i-1][j] = 'V'
                        if prev_grid[i-1][j-1] == '.':
                            new_grid[i-1][j-1] = 'V'
                    else:
                        if prev_grid[i-1][j-1] == '.':
                            new_grid[i-1][j-1] = 'V'
                        if prev_grid[i-1][j] == '.':
                            new_grid[i-1][j] = 'V'
                        if prev_grid[i-1][j+1] == '.':
                            new_grid[i-1][j+1] = 'V'
                else:
                    if prev_grid[i-1][j] == '.':
                        new_grid[i-1][j] = 'V'
                    elif prev_grid[i-1][j] == '#':
                        if j == 0:
                            if prev_grid[i][j+1] == '.':
                                new_grid[i][j+1] = 'V'
                        elif j == M-1:
                            if prev_grid[i][j-1] == '.':
                                new_grid[i][j-1] = 'V'
                        else:
                            if prev_grid[i][j-1] == '.':
                                new_grid[i][j-1] = 'V'
                            if prev_grid[i][j+1] == '.':
                                new_grid[i][j+1] = 'V'
    prev_grid = new_grid
    
    # print grid
    for row in prev_grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
