import sys

def main():
    words = []
    for line in sys.stdin:
        for word in line.split():
            if word in words:
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.append(word)
        print()

main()
