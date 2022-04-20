# https://codeforces.com/problemset/problem/1221/A

n, m = map(int, input().split())
grid = []
stars = 0
for i in range(n):
    grid.append(input())
    for j in range(m):
        if grid[i][j] == '*':
            stars += 1

if stars == 0:
    print(0)
    exit()

# find start star
i, j = 0, 0
while i < n:
    if grid[i][j] == '*':
        break
    j += 1
    if j == m:
        j = 0
        i += 1

# find star width and height
star_width = 0
while j + star_width < m and grid[i][j + star_width] == '*':
    star_width += 1
star_height = 0
while i + star_height < n and grid[i + star_height][j] == '*':
    star_height += 1

# check if star is valid
if star_width == 0 or star_height == 0:
    print(-1)
    exit()

# check if all stars are valid
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*' and (i < (star_height - 1) or i >= n - (star_height - 1) or j < (star_width - 1) or j >= m - (star_width - 1)):
            print(-1)
            exit()

# print the stars and the star size
print(stars, min(star_width, star_height))
