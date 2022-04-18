import sys
import math

def main():
    lines = sys.stdin.readlines()
    n, m = map(int, lines[0].split())
    grid = [list(line.rstrip()) for line in lines[1:]]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                if i == 0:
                    if j == 0:
                        if grid[i+1][j] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'X'
                    elif j == m-1:
                        if grid[i+1][j] == '.' or grid[i][j-1] == '.':
                            grid[i][j] = 'X'
                    else:
                        if grid[i+1][j] == '.' or grid[i][j-1] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'X'
                elif i == n-1:
                    if j == 0:
                        if grid[i-1][j] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'X'
                    elif j == m-1:
                        if grid[i-1][j] == '.' or grid[i][j-1] == '.':
                            grid[i][j] = 'X'
                    else:
                        if grid[i-1][j] == '.' or grid[i][j-1] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'X'
                else:
                    if j == 0:
                        if grid[i-1][j] == '.' or grid[i+1][j] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'X'
                    elif j == m-1:
                        if grid[i-1][j] == '.' or grid[i+1][j] == '.' or grid[i][j-1] == '.':
                            grid[i][j] = 'X'
                    else:
                        if grid[i-1][j] == '.' or grid[i+1][j] == '.' or grid[i][j-1] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'X'
    for i in range(n):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
