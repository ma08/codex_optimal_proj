
import sys
import math

def main():
    line = sys.stdin.readline().strip().split(' ')
    R = int(line[0])
    C = int(line[1])
    crossword = [sys.stdin.readline().strip() for i in range(R)]
    words = list()
    for i in range(R):
        words.extend([word for word in crossword[i].split('#') if len(word) >= 2])
    for j in range(C):
        words.extend([word for word in ''.join([crossword[i][j] for i in range(R)]).split('#') if len(word) >= 2])
    words.sort()
    print(words[0])

if __name__ == '__main__':
    main()
