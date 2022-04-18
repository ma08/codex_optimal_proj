#!/usr/bin/env python3

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # spread water starting from the bottom row
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

    # print final grid
    for i in range(N):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
