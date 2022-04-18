
import sys

def main():
    line = sys.stdin.readline().strip().split(' ')
    R = int(line[0])
    C = int(line[1])
    crossword = [sys.stdin.readline().strip() for i in range(R)]
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
        if len(word) >= 2 and word not in words:
            words.append(word)
    for j in range(1, C):
        word = ''
        for i in range(R):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2 and word not in words:
            words.append(word)
    words.sort()
    print(words[0])

if __name__ == '__main__':
    main()
