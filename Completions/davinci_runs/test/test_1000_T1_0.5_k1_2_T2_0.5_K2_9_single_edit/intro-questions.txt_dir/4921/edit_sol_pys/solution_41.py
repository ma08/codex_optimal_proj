
import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().split()
        for word in line:
            if word.lower() not in words:
                words.append(word.lower())
                print(word, end=' ')
            else:
                print('.', end=' ')
        print('')

main()
