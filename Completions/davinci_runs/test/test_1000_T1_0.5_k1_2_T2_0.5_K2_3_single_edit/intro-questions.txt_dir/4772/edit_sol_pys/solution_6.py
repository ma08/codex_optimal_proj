import sys

def main():
    R, C = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(R)]
    words = []

    # horizontal words
    for row in grid:
        word = []
        for i in range(len(row)):
            if row[i] == '#':
                if len(word) > 0:
                    words.append(''.join(word))
                word = []
            else:
                word += char
        if len(word) > 1:
            words.append(word)

    # vertical words
    for col in range(C):
        word = ''
        for row in range(R):
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

if __name__ == '__main__':
    main()
