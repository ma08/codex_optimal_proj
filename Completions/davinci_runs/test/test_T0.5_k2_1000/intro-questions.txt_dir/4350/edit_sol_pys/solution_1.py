import numpy as np

def solve(grid):
    n, m = grid.shape
    grid = grid.copy()  # make a copy of the grid
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i,j] == '*':
                s = 1
                while i+s < n and j+s < m:
                    if grid[i+s,j+s] == '*':
                        s += 1
                    else:
                        break
                if s > 1:
                    grid[i:i+s,j:j+s] = '.'
                    stars.append([i+1,j+1,s])
    # check if all stars are removed
    for i in range(n):
        for j in range(m):
            if grid[i,j] == '*':
                return -1
    return stars  # return the list of stars

def main():
    n, m = map(int, input().split())
    grid = np.array([list(input()) for _ in range(n)])  # read the grid
    stars = solve(grid)
    if stars == -1:  # if there is no solution
        print(-1)
    else:  # if there is a solution
        print(len(stars))
        for s in stars:
            print(*s)

if __name__ == '__main__':
    main()
