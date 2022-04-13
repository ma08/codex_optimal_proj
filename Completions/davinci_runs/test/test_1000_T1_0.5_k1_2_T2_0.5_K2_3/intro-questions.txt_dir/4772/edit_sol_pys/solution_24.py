
import sys


def main():
    R, C = map(int, sys.stdin.readline().split())
    crossword = []
    for i in range(R):
        row = sys.stdin.readline().strip().split()
        crossword.append(row)

    smallest_word = 'zz'
    for row in range(R):
        for col in range(C):
            if crossword[row][col] != '#':
                if row + 1 < R:
                    if crossword[row + 1][col] != '#':
                        word = crossword[row][col] + crossword[row + 1][col]
                        smallest_word = min(smallest_word, word)
                if col + 1 < C:
                    if crossword[row][col + 1] != '#':
                        word = crossword[row][col] + crossword[row][col + 1]
                        smallest_word = min(smallest_word, word)

    print(smallest_word)


if __name__ == '__main__':
    main()
