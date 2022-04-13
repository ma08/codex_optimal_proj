#!/usr/bin/python3

import sys

def main(file):
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(n):
        grid.append(sys.stdin.readline().strip())

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                grid[i] = grid[i][:j] + 'E' + grid[i][j+1:m]
                if i > 0 and grid[i-1][j] == '.':
                    grid[i-1] = grid[i-1][:j] + 'E' + grid[i-1][j+1:m]
                if j > 0 and grid[i][j-1] == '.':
                    grid[i] = grid[i][:j-1] + 'E' + grid[i][j:m]
                if i < n-1 and grid[i+1][j] == '.':
                    grid[i+1] = grid[i+1][:j] + 'E' + grid[i+1][j+1:m]
                if j < m-1 and grid[i][j+1] == '.':
                    grid[i] = grid[i][:j+1] + 'E' + grid[i][j+2:m]
    for i in range(n):
        print(grid[i])

main(sys.argv[1])
