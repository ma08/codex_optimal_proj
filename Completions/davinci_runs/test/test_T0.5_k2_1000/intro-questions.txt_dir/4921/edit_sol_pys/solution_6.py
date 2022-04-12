
#!/usr/bin/env python3
import sys

def main(argv):
    words = set()
    for line in sys.stdin:
        for word in line.split():
            if word.lower() in words:
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.add(word.lower())
        print()

main(sys.argv)
