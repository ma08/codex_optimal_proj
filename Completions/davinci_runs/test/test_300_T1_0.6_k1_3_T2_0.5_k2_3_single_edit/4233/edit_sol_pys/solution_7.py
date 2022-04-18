

n, m = map(int, input().split()) # get the size of the grid
grid = []
for _ in range(n): # get the grid
    row = list(input())
    grid.append(row)

stars = [] # list of all stars
# stars = [ [x, y, size, col, row] ] # stars = [ [x, y, size] ]

def add_star(x, y, size):
    # print("add_star", x, y, size)
    stars.append([x, y, size])

def check_star(x, y, size):
    # print("check_star", x, y, size)
    for i in range(size):
        for j in range(size):
            if grid[x+i][y+j] == '.':
                return False
    return True

def check_stars():
    for star in stars:
        x, y, size, col, row = star
        for i in range(size):
            for j in range(size):
                if grid[x+i][y+j] != '*':
                    return False
    return True

def remove_star(x, y, size, col, row):
    # print("remove_star", x, y, size, col, row)
    stars.remove([x, y, size, col, row])

def find_stars():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                add_star(i, j, 1, False, False)
                if i+1 < n and check_star(i, j, 2, False, False):
                    add_star(i, j, 2, False, False)
                if j+1 < m and check_star(i, j, 2, True, False):
                    add_star(i, j, 2, True, False)
                if i+1 < n and j+1 < m and check_star(i, j, 2, True, True):
                    add_star(i, j, 2, True, True)
                if i+2 < n and check_star(i, j, 3, False, False):
                    add_star(i, j, 3, False, False)
                if j+2 < m and check_star(i, j, 3, True, False):
                    add_star(i, j, 3, True, False)
                if i+2 < n and j+2 < m and check_star(i, j, 3, True, True):
                    add_star(i, j, 3, True, True)

def print_stars():
    for star in stars:
        x, y, size, col, row = star
        print(x+1, y+1, size)

def remove_stars():
    for star in stars:
        x, y, size, col, row = star
        for i in range(size):
            for j in range(size):
                grid[x+i][y+j] = '.'

def fill_stars():
    for star in stars:
        x, y, size, col, row = star
        for i in range(size):
            for j in range(size):
                grid[x+i][y+j] = '*'

find_stars()
if check_stars():
    print(len(stars))
    print_stars()
else:
    print(-1)
