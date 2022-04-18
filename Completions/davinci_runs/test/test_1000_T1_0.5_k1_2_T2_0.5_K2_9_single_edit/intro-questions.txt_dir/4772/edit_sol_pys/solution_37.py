

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
    for i in range(r):
        for j in range(c):
            if crossword[i][j] != '#':
                if i + 1 < r:
                    if crossword[i + 1][j] != '#':
                        word = crossword[i][j] + crossword[i + 1][j]
                        if word < smallest_word:
                            smallest_word = word
                if j + 1 < c:
                    if crossword[i][j + 1] != '#':
                        word = crossword[i][j] + crossword[i][j + 1]
                        if word < smallest_word:
                            smallest_word = word

    print(smallest_word)


if __name__ == '__main__':
    main()
