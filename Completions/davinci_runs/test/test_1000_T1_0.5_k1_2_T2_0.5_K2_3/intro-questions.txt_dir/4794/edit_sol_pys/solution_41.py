

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
squashed = [0]*5
for space in possible_spaces:
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
            squashed[0] += 1
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
            squashed[1] += 1
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
            squashed[2] += 1
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
            squashed[3] += 1
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
            squashed[4] += 1

# print the number of spaces that squish 0, 1, 2, 3, and 4 cars
for i in range(5):
    print(squash.count(i))
