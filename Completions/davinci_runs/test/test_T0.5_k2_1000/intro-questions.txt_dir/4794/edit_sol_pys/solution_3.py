

R, C = map(int, input().split())
grid = [input() for i in range(R)]

# find all possible parking spaces
possible_spaces = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == '.':
            if i <= R-2 and j <= C-2:
                possible_spaces.append([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])

# count the number of cars to be squished for each space
squish = [0]*5
for space in possible_spaces:
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
            squish[0] += 1
    for cell in space[1:]:
        if grid[cell[0]][cell[1]] == 'X' and grid[cell[0]-1][cell[1]-1] == 'X':
            squish[1] += 1 
    for cell in space[2:]:
        if grid[cell[0]][cell[1]] == 'X' and grid[cell[0]-1][cell[1]-1] == 'X' and grid[cell[0]-2][cell[1]-2] == 'X':
            squish[2] += 1
    for cell in space[3:]:
        if grid[cell[0]][cell[1]] == 'X' and grid[cell[0]-1][cell[1]-1] == 'X' and grid[cell[0]-2][cell[1]-2] == 'X' and grid[cell[0]-3][cell[1]-3] == 'X':
            squish[3] += 1
    for cell in space[4:]:
        if grid[cell[0]][cell[1]] == 'X' and grid[cell[0]-1][cell[1]-1] == 'X' and grid[cell[0]-2][cell[1]-2] == 'X' and grid[cell[0]-3][cell[1]-3] == 'X' and grid[cell[0]-4][cell[1]-4] == 'X':
            squish[4] += 1

# print the number of spaces that squish 0, 1, 2, 3, and 4 cars
for i in range(5):
    print(squish.count(i))
