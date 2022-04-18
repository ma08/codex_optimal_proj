
import sys

r, c = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().strip() for _ in range(r)]
words = []

# horizontal words
for row in grid:
    word = ''
    for char in row:
        if char == '#':
            if len(word) > 1:
                words.append(word)
            word = ''
        else:
            word += char
    if len(word) > 1:
        words.append(word)

# vertical words
for col in range(c):
    word = ''
    for row in range(r):
        char = grid[row][col]
        if char == '#':
            if len(word) > 1:
                words.append(word)
            word = ''
        else:
            word += char
    if len(word) > 1:
        words.append(word)

print(sorted(words)[0])
