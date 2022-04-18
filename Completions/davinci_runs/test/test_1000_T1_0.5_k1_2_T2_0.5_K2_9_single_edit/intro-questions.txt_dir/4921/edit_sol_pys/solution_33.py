
import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().split(' ')
        for i, word in enumerate(line):
            if word.lower() in words:
                line[i] = '.'
            words.append(word.lower())
        print(' '.join(line))

main()
