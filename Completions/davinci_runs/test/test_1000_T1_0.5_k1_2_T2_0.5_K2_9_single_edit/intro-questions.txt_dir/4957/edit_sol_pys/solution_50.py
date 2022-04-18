import sys

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
                            grid[i][j] = 'E'
                    elif j == m-1:
                        if grid[i+1][j] == '.' or grid[i][j-1] == '.':
                            grid[i][j] = 'E'
                    else:
                        if grid[i+1][j] == '.' or grid[i][j-1] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'E'
                elif i == n-1:
                    if j == 0:
                        if grid[i-1][j] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'E'
                    elif j == m-1:
                        if grid[i-1][j] == '.' or grid[i][j-1] == '.':
                            grid[i][j] = 'E'
                    else:
                        if grid[i-1][j] == '.' or grid[i][j-1] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'E'
                else:
                    if j == 0:
                        if grid[i-1][j] == '.' or grid[i+1][j] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'E'
                    elif j == m-1:
                        if grid[i-1][j] == '.' or grid[i+1][j] == '.' or grid[i][j-1] == '.':
                            grid[i][j] = 'E'
                    else:
                        if grid[i-1][j] == '.' or grid[i+1][j] == '.' or grid[i][j-1] == '.' or grid[i][j+1] == '.':
                            grid[i][j] = 'E'
    for i in range(n):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
