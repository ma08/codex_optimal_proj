def main():
    n,m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    stars = []
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == '*'):
                if(i > 0 and j > 0 and grid[i-1][j-1] == '*') or (i > 0 and grid[i-1][j] == '*') or (i > 0 and j < m-1 and grid[i-1][j+1] == '*') or (j > 0 and grid[i][j-1] == '*') or (j < m-1 and grid[i][j+1] == '*') or (i < n-1 and j > 0 and grid[i+1][j-1] == '*') or (i < n-1 and grid[i+1][j] == '*') or (i < n-1 and j < m-1 and grid[i+1][j+1] == '*'):
                    stars.append([i+1, j+1, 1])
    if(len(stars) == 0):
        print('-1')
        return
    print(len(stars))
    for i in range(len(stars)):
        print(stars[i][0], stars[i][1], stars[i][2])
main()
