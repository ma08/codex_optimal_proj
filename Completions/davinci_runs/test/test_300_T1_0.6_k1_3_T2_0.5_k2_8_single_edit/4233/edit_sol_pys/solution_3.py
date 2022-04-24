
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(input())
    grid.append(row)

stars = []
# stars = [ [x, y, size, col, row, id] ]

def add_star(x, y, size, col, row, id):
    # print("add_star", x, y, size, col, row)
    stars.append([x, y, size, col, row, id])

def check_star(x, y, size, col, row, id):
    if id in [star[5] for star in stars]:
        return False
    # print("check_star", x, y, size, col, row)
    for i in range(size):
        for j in range(size):
            if grid[x+i][y+j] == '.':
                return False
    return True

def check_stars():
    for star in stars:
        x, y, size, col, row, id = star
        for i in range(size):
            for j in range(size):
                if grid[x+i][y+j] != '*':
                    return False
    return True

def remove_star(x, y, size, col, row, id):
    # print("remove_star", x, y, size, col, row)
    stars.remove([x, y, size, col, row, id])

def find_stars():
    id = 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                add_star(i, j, 1, False, False, id)
                id += 1
                if i+1 < n and check_star(i, j, 2, False, False, id):
                    add_star(i, j, 2, False, False, id)
                    id += 1
                if j+1 < m and check_star(i, j, 2, True, False, id):
                    add_star(i, j, 2, True, False, id)
                    id += 1
                if i+1 < n and j+1 < m and check_star(i, j, 2, True, True, id):
                    add_star(i, j, 2, True, True, id)
                    id += 1
                if i+2 < n and check_star(i, j, 3, False, False, id):
                    add_star(i, j, 3, False, False, id)
                    id += 1
                if j+2 < m and check_star(i, j, 3, True, False, id):
                    add_star(i, j, 3, True, False, id)
                    id += 1
                if i+2 < n and j+2 < m and check_star(i, j, 3, True, True, id):
                    add_star(i, j, 3, True, True, id)
                    id += 1

def print_stars():
    for star in stars:
        x, y, size, col, row, id = star
        print(x+1, y+1, size)

def remove_stars():
    for star in stars:
        x, y, size, col, row, id = star
        for i in range(size):
            for j in range(size):
                grid[x+i][y+j] = '.'

def fill_stars():
    for star in stars:
        x, y, size, col, row, id = star
        for i in range(size):
            for j in range(size):
                grid[x+i][y+j] = '*'

find_stars()
if check_stars():
    print(len(stars))
    print_stars()
else:
    print(-1)
