
import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip()
        for word in line.split():
            if word.lower() not in words:
                print(word, end=' ')
                words.append(word.lower())
            else:
                print('.', end=' ')
        print()

#main()
