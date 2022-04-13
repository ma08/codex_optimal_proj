

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # each cell is either air, stone, or water (1, 2, 3)
    # water spreads:
    # * if water cell is above air cell, air cell turns into water (1 -> 3)
    # * if water cell is above stone cell, air cells left and right of water cell turn into water (1 -> 3)
    # * each second
    # * water stops spreading
    # print grid when water stops spreading
    # assume that all cells outside of the grid behave as air cells
    #   e.g. if water cell is at bottommost row, water will not spread to the sides
    #
    # grid is N rows and M columns
    # 2 <= N, M <= 50
    #
    # each of N lines contains a string S of length M
    # S represents one of the rows in the grid
    # S consists of the symbols "1", "2", and "3"
    #   1 = air
    #   2 = stone
    #   3 = water
    
    # spread water
    for i in range(N-1, -1, -1):
        for j in range(M):
            if grid[i][j] == '3':
                if i == N-1:
                    if j == 0:
                        if grid[i-1][j] == '1':
                            grid[i-1][j] = '3'
                        if grid[i-1][j+1] == '1':
                            grid[i-1][j+1] = '3'
                    elif j == M-1:
                        if grid[i-1][j] == '1':
                            grid[i-1][j] = '3'
                        if grid[i-1][j-1] == '1':
                            grid[i-1][j-1] = '3'
                    else:
                        if grid[i-1][j-1] == '1':
                            grid[i-1][j-1] = '3'
                        if grid[i-1][j] == '1':
                            grid[i-1][j] = '3'
                        if grid[i-1][j+1] == '1':
                            grid[i-1][j+1] = '3'
                else:
                    if grid[i-1][j] == '1':
                        grid[i-1][j] = '3'
                    elif grid[i-1][j] == '2':
                        if j == 0:
                            if grid[i][j+1] == '1':
                                grid[i][j+1] = '3'
                        elif j == M-1:
                            if grid[i][j-1] == '1':
                                grid[i][j-1] = '3'
                        else:
                            if grid[i][j-1] == '1':
                                grid[i][j-1] = '3'
                            if grid[i][j+1] == '1':
                                grid[i][j+1] = '3'
    
    # print grid
    for i in range(N):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
