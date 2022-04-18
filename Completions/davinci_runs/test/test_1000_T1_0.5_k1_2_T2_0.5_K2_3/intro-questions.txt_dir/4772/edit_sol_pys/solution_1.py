
import sys

def main():
    R, C = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(R)]
    words = []

    # horizontal words
    for row in grid:
        word = ''
        for c in row:
            if c == '#':
                if len(word) > 1:
                    words.append(word)
                word = ''
            else:
                word += c
        if len(word) > 1:
            words.append(word)

    # vertical words
    for col in range(C):
        word = ''
        for row in range(R):
            c = grid[row][col]
            if c == '#':
                if len(word) > 1:
                    words.append(word)
                word = ''
            else:
                word += c
        if len(word) > 1:
            words.append(word)

    print(sorted(words)[0])

if __name__ == '__main__':
    main()
