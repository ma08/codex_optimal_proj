
import sys

def main():
    words = set()
    for line in sys.stdin:
        for word in line.split():
            if word.lower() in words:
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.add(word.lower())
        print()
main()
