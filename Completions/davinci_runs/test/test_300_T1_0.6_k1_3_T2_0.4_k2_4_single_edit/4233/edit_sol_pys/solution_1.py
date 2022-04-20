
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(input())
    grid.append(row)

stars = []
# stars = [ [x, y, size, col, row, found] ]

def add_star(x, y, size, col, row):
    # print("add_star", x, y, size, col, row)
    stars.append([x, y, size, col, row, False])

def check_star(x, y, size, col, row):
    # print("check_star", x, y, size, col, row)
    for i in range(size):
        for j in range(size):
            if grid[x+i][y+j] == '.':
                return False
    return True

def check_stars():
    for star in stars:
        x, y, size, col, row, found = star
        for i in range(size):
            for j in range(size):
                if grid[x+i][y+j] != '*':
                    return False
    return True

def remove_star(x, y, size, col, row):
    # print("remove_star", x, y, size, col, row)
    stars.remove([x, y, size, col, row, False])

def find_stars():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                add_star(i, j, 1, False, False, False)
                if i+1 < n and check_star(i, j, 2, False, False, False):
                    add_star(i, j, 2, False, False, False)
                if j+1 < m and check_star(i, j, 2, True, False, False):
                    add_star(i, j, 2, True, False, False)
                if i+1 < n and j+1 < m and check_star(i, j, 2, True, True, False):
                    add_star(i, j, 2, True, True, False)
                if i+2 < n and check_star(i, j, 3, False, False, False):
                    add_star(i, j, 3, False, False, False)
                if j+2 < m and check_star(i, j, 3, True, False, False):
                    add_star(i, j, 3, True, False, False)
                if i+2 < n and j+2 < m and check_star(i, j, 3, True, True, False):
                    add_star(i, j, 3, True, True, False)

def print_stars():
    for star in stars:
        x, y, size, col, row, found = star
        print(x+1, y+1, size)

def remove_stars():
    for star in stars:
        x, y, size, col, row, found = star
        for i in range(size):
            for j in range(size):
                grid[x+i][y+j] = '.'

def fill_stars():
    for star in stars:
        x, y, size, col, row, found = star
        for i in range(size):
            for j in range(size):
                grid[x+i][y+j] = '*'

find_stars()
if check_stars():
    print(len(stars))
    print_stars()
else:
    print(-1)
