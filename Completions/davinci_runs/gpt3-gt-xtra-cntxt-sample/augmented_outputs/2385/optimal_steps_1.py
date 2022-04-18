import sys

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(input()))
        directions = []
        for _ in range(n):
            directions.append(list(input()))
        black_cells = 0
        white_cells = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    black_cells += 1
                else:
                    white_cells += 1
        num_robots = 0
        for i in range(n):
            for j in range(m):
                if directions[i][j] == 'U':
                    if i != 0:
                        if grid[i-1][j] == '1':
                            num_robots += 1
                elif directions[i][j] == 'R':
                    if j != m-1:
                        if grid[i][j+1] == '1':
                            num_robots += 1
                elif directions[i][j] == 'D':
                    if i != n-1:
                        if grid[i+1][j] == '1':
                            num_robots += 1
                elif directions[i][j] == 'L':
                    if j != 0:
                        if grid[i][j-1] == '1':
                            num_robots += 1
        max_black = min(num_robots, black_cells)
        print(num_robots, max_black)

if __name__ == "__main__":
    main()