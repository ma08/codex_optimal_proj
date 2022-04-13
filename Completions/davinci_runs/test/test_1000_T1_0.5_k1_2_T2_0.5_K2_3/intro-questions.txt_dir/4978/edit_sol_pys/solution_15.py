
def get_input():
    n, m = [int(i) for i in input().split()]

    grid = []
    for i in range(n):
        grid.append(input())
    
    return grid

def print_output(grid):
    for i in range(len(grid)):
        print(grid[i])

def move_virus(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'V':
                if i-1 >= 0:
                    if grid[i-1][j] == '.':
                        grid[i-1] = grid[i-1][:j] + "V" + grid[i-1][j+1:]
                    if grid[i-1][j] == '#':
                        if (j-1 >= 0) and (grid[i][j-1] == '.'):
                            grid[i] = grid[i][:j-1] + "V" + grid[i][j:]
                        if (j+1 < len(grid[i])) and (grid[i][j+1] == '.'):
                            grid[i] = grid[i][:j+1] + "V" + grid[i][j+2:]

if __name__ == "__main__":
    grid = get_input()
    move_virus(grid)
    print_output(grid)
