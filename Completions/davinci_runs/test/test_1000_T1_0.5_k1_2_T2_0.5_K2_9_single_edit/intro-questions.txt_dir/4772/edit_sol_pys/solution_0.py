import sys

def main():
    R, C = sys.stdin.readline().split()
    R = int(R)
    C = int(C)
    crossword = []
    for i in range(R):
        row = sys.stdin.readline().strip()
        crossword.append(row)
    smallest_word = 'z'
    for r in range(R):
        for c in range(C):
            if crossword[r][c] != '#':
                if r + 1 < R:
                    if crossword[r + 1][c] != '#':
                        word = crossword[r][c] + crossword[r + 1][c]
                        if word < smallest_word:
                            smallest_word = word
                if c + 1 < C:
                    if crossword[r][c + 1] != '#':
                        word = crossword[r][c] + crossword[r][c + 1]
                        if word < smallest_word:
                            smallest_word = word
    print(smallest_word)

if __name__ == '__main__':
    main()
