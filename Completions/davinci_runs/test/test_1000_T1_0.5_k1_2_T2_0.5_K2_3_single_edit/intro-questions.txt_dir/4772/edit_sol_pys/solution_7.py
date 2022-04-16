





# Accepted after 2nd attempt (wrong answer on first attempt)

# Read input
R, C = [int(i) for i in input().split()]
grid = []
for i in range(R):
    grid.append(list(input()))

# Find all words
words = []
for r in range(R):
    for c in range(C):
        # Check horizontal
        if c < C-1 and grid[r][c] != '#' and grid[r][c+1] != '#':
            word = grid[r][c]
            while c < C-1 and grid[r][c+1] != '#':
                c += 1
                word += grid[r][c]
            if len(word) > 1:
                words.append(word)

        # Check vertical
        if r < R-1 and grid[r][c] != '#' and grid[r+1][c] != '#':
            word = grid[r][c]
            while r < R-1 and grid[r+1][c] != '#':
                r += 1
                word += grid[r][c]
            if len(word) > 1:
                words.append(word)

# Print lexicographically smallest word
print(min(words))
