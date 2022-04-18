import sys
import re

def main():
    words = set()
    for line in sys.stdin:
        for word in re.split(r'\W+', line):
            if word.lower() in words or len(word) < 3:
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.add(word.lower())
        print()

main()
