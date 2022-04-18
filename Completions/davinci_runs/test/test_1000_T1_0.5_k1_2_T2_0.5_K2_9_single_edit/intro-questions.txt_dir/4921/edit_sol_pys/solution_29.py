

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            if word.lower() not in words:
                print(word, end=' ')
                words.append(word.lower())
            else:
                print('.', end=' ')
        print()

#main()
