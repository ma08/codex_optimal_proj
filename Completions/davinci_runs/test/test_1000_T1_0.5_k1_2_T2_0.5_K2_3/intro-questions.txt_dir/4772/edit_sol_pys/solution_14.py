import sys


def main():
    r, c = sys.stdin.readline().split()
    r = int(r)
    c = int(c)
    crossword = []
    for i in range(r):
        row = sys.stdin.readline().strip()
        crossword.append(row)

    smallest_word = 'z'
    for r in range(r):
        for c in range(c):
            if crossword[r][c] != '#':
                if r + 1 < r:
                    if crossword[r + 1][c] != '#':
                        word = crossword[r][c] + crossword[r + 1][c]
                        if word < smallest_word:
                            smallest_word = word
                if c + 1 < c:
                    if crossword[r][c + 1] != '#':
                        word = crossword[r][c] + crossword[r][c + 1]
                        if word < smallest_word:
                            smallest_word = word

    print(smallest_word)


if __name__ == '__main__':
    main()
