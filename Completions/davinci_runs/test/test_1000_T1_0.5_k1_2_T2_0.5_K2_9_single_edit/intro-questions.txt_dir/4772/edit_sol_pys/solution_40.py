
import sys

def main():
    line = sys.stdin.readline().strip().split(' ')
    r = int(line[0])
    c = int(line[1])
    crossword = list()
    for i in range(r):
        crossword.append(sys.stdin.readline().strip())
    words = list()
    for i in range(r):
        word = ''
        for j in range(c):
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
        for i in range(r):
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
