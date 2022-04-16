
import numpy as np

def solve(grid):
    n, m = grid.shape
    grid = grid.copy()
    stars = 0
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
                    stars += 1
    for i in range(n):
        for j in range(m):
            if grid[i,j] == '*':
                return -1
    return stars

def main():
    n, m = map(int, input().split())
    grid = np.array([list(input()) for _ in range(n)])
    stars = solve(grid)
    if stars == -1:
        print(-1)
    else:
        print(stars)

if __name__ == '__main__':
    main()
