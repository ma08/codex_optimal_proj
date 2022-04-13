import sys, os

def main():
    words = []
    if os.path.isfile(sys.argv[1]):
        f = open(sys.argv[1])
    else:
        f = sys.stdin
    for line in f:
        for word in line.split():
            if word.lower() not in words:
                words.append(word.lower())
                print(word, end=' ')
            else:
                print('.', end=' ')
        print()

if __name__ == "__main__":
    main()
