

#-----Solution-----

def draw(grid, n, m):
    stars = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars += 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                s = 1
                while i+s < n and j+s < m and grid[i+s][j] == '*' and grid[i][j+s] == '*' and grid[i+s][j+s] == '*':
                    s += 1
                for k in range(s):
                    for l in range(s):
                        if grid[i+k][j+l] == '*':
                            grid[i+k][j+l] = '.'
                        else:
                            return -1
    if stars == n*m:
        return 0
    else:
        return stars

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

stars = draw(grid, n, m)
if stars == -1:
    print(-1)
else:
    print(stars)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                s = 1
                while i+s < n and j+s < m and grid[i+s][j] == '*' and grid[i][j+s] == '*' and grid[i+s][j+s] == '*':
                    s += 1
                print(i+1, j+1, s)
                for k in range(s):
                    for l in range(s):
                        grid[i+k][j+l] = '.'