

def stars(n, m):
    grid = []
    for i in range(n):
        grid.append(list(input()))
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                print('.', end='')
            else:
                c = 0
                if i - 1 >= 0 and grid[i - 1][j] == '*':
                    c += 1
                if i + 1 < n and grid[i + 1][j] == '*':
                    c += 1
                if j + 1 < m and grid[i][j + 1] == '*':
                    c += 1
                if j - 1 >= 0 and grid[i][j - 1] == '*':
                    c += 1
                if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == '*':
                    c += 1
                if i - 1 >= 0 and j + 1 < m and grid[i - 1][j + 1] == '*':
                    c += 1
                if i + 1 < n and j - 1 >= 0 and grid[i + 1][j - 1] == '*':
                    c += 1
                if i + 1 < n and j + 1 < m and grid[i + 1][j + 1] == '*':
                    c += 1
                print(c, end='')
        print('')



n, m = map(int, input().split())
stars(n, m)
