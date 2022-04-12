

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # each cell is either air, stone, or water
    # water spreads:
    # * if water cell is above air cell, air cell turns into water
    # * if water cell is above stone cell, air cells left or right of water cell turn into water if they exist
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
    for i in range(N-1, -1, -1):
        for j in range(M):
            if grid[i][j] == 'V':
                if i == N-1:
                    if j == 0:
                        if grid[i-1][j] == '.':
                            grid[i-1][j] = 'V'
                        if grid[i-1][j+1] == '.':
                            grid[i-1][j+1] = 'V'
                    elif j == M-1:
                        if grid[i-1][j] == '.':
                            grid[i-1][j] = 'V'
                        if grid[i-1][j-1] == '.':
                            grid[i-1][j-1] = 'V'
                    else:
                        if grid[i-1][j-1] == '.':
                            grid[i-1][j-1] = 'V'
                        if grid[i-1][j] == '.':
                            grid[i-1][j] = 'V'
                        if grid[i-1][j+1] == '.':
                            grid[i-1][j+1] = 'V'
                else:
                    if grid[i-1][j] == '.':
                        grid[i-1][j] = 'V'
                    elif grid[i-1][j] == '#':
                        if j == 0:
                            if grid[i][j+1] == '.':
                                grid[i][j+1] = 'V'
                        elif j == M-1:
                            if grid[i][j-1] == '.':
                                grid[i][j-1] = 'V'
                        else:
                            if grid[i][j-1] == '.':
                                grid[i][j-1] = 'V'
                            if grid[i][j+1] == '.':
                                grid[i][j+1] = 'V'
    
    # print grid
    for i in range(N):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
