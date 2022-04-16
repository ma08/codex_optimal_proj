import sys


def main():
    words = {}
    for line in sys.stdin:
        for word in line.split():
            if word.lower() not in words:
                words[word.lower()] = True
                print(word, end=' ')
            else:
                print('.', end=' ')
        print()

if __name__ == "__main__":
    main()
