

from collections import Counter

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
squished = []
for space in possible_spaces:
    for cell in space:
        if grid[cell[0]][cell[1]] == 'X':
    squished.append(squished.count('X'))

# count the number of spaces that squish 0, 1, 2, 3, and 4 cars
squished_counts = Counter(squished)
for i in range(5): print(squished_counts[i])
