

import sys


def main():
    row, col = sys.stdin.readline().split()
    row = int(row)
    col = int(col)
    crossword = []
    for i in range(row):
        row = sys.stdin.readline().strip()
        crossword.append(row)

    smallest_word = 'z'
    for r in range(row):
        for c in range(col):
            if crossword[r][c] != "#":
                if r + 1 < row:
                    if crossword[r + 1][c] != "#":
                        word = crossword[r][c] + crossword[r + 1][c] + crossword[r + 2][c]
                        if word < smallest_word:
                            smallest_word = word
                if c + 1 < col:
                    if crossword[r][c + 1] != "#":
                        word = crossword[r][c] + crossword[r][c + 1]
                        if word < smallest_word:
                            smallest_word = word

    print(smallest_word)


if __name__ == '__main__':
    main()
