#!/usr/bin/env python3

import sys
import math

def main():
    line = sys.stdin.readline().split(' ')
    R = int(line[0])
    C = int(line[1])
    crossword = list()
    for i in range(R):
        crossword.append(sys.stdin.readline())
    words = list()
    for i in range(R):
        word = ''
        for j in range(C):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    for j in range(C):
        word = ''
        for i in range(R):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    words.sort()
    print(words[0])

if __name__ == '__main__':
    main()
