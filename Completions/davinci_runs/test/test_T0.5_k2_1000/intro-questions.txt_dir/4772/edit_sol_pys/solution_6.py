
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip().split(' ')
        R = int(line[0])
        C = int(line[1])
        crossword = list()
        for j in range(R):
            crossword.append(sys.stdin.readline().strip())
        words = list()
        for k in range(R):
            word = ''
            for l in range(C):
                if crossword[k][l] != '#':
                    word += crossword[k][l]
                else:
                    if len(word) >= 2:
                        words.append(word)
                    word = ''
            if len(word) >= 2:
                words.append(word)
        for m in range(C):
            word = ''
            for n in range(R):
                if crossword[n][m] != '#':
                    word += crossword[n][m]
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
