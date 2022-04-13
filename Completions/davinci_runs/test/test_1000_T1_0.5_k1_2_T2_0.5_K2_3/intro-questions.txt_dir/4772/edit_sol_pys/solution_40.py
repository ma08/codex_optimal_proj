import sys


def get_smallest_word(r, c, crossword):
    smallest_word = 'z'

    if r - 1 >= 0:
        if crossword[r - 1][c] != '#':
            word = crossword[r - 1][c] + crossword[r][c]
            if word < smallest_word:
                smallest_word = word
    if r + 1 < len(crossword):
        if crossword[r + 1][c] != '#':
            word = crossword[r][c] + crossword[r + 1][c]
            if word < smallest_word:
                smallest_word = word
    if c - 1 >= 0:
        if crossword[r][c - 1] != '#':
            word = crossword[r][c - 1] + crossword[r][c]
            if word < smallest_word:
                smallest_word = word
    if c + 1 < len(crossword[0]):
        if crossword[r][c + 1] != '#':
            word = crossword[r][c] + crossword[r][c + 1]
            if word < smallest_word:
                smallest_word = word

    return smallest_word


def main():
    R, C = sys.stdin.readline().split()
    R = int(R)
    C = int(C)
    crossword = []
    for i in range(R):
        row = sys.stdin.readline().strip()
        crossword.append(row)

    smallest_word = 'zz'
    for r in range(R):
        for c in range(C):
            if crossword[r][c] != '#':
                word = get_smallest_word(r, c, crossword)
                if word < smallest_word:
                    smallest_word = word

    print(smallest_word)


if __name__ == '__main__':
    main()
