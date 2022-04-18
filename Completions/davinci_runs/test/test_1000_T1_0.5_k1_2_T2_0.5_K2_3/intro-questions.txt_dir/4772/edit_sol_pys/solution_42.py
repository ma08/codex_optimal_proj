import sys
import math

def main():
    line = sys.stdin.readline().strip().split(' ')
    R = int(line[0])
    C = int(line[1])
    crosswords = list()
    for i in range(R):
        crosswords.append(sys.stdin.readline().strip())
    words = list()
    for i in range(R):
        word = ''
        for j in range(C):
            if crosswords[i][j] != '#':
                word += crosswords[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    for j in range(C):
        word = ''
        for i in range(R):
            if crosswords[i][j] != '#':
                word += crosswords[i][j]
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
