

import sys

def main():
    words = []
    unique = []
    for line in sys.stdin:
        words.extend(line.split())

    for word in words:
        if word.lower() not in unique:
            unique.append(word.lower())
            print(word, end=' ')
        else:
            print('.', end=' ')
    print()

if __name__ == '__main__':
    main()
