
import sys

def main():
    r, c = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(r)]
    words = set()

    # horizontal words.
    for row in grid:
        word = ''
        for char in row:
            if char == '#':
                if len(word) > 1:
                    words.add(word)
                word = ''
            else:
                word += char
        if len(word) > 1:
            words.add(word)

    # vertical words
    for col in range(c):
        word = ''
        for row in range(r):
            char = grid[row][col]
            if char == '#':
                if len(word) > 1:
                    words.add(word)
                word = ''
            else:
                word += char
        if len(word) > 1:
            words.add(word)

    print(sorted(words)[0])

if __name__ == '__main__':
    main()
