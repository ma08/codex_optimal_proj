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
    for row in range(r):
        for col in range(c):
            if crossword[row][col] != '#':
                if row + 1 < r:
                    if crossword[row + 1][col] != '#':
                        word = crossword[row][col] + crossword[row + 1][col]
                        if word < smallest_word:
                            smallest_word = word
                if col + 1 < c:
                    if crossword[row][col + 1] != '#':
                        word = crossword[row][col] + crossword[row][col + 1]
                        if word < smallest_word:
                            smallest_word = word

    print(smallest_word)


if __name__ == '__main__':
    main()
