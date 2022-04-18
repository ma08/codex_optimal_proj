

import sys, math

def main():
    N = int(input())
    if N == 1:
        print(0)
        return

    # horizontal words
    for row in grid:
        word = ''
        for char in row:
            if char == '#':
                if len(word) > 1:
                    words.append(word)
                word = ''
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
