

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.split()
        for word in line:
            if word.lower() in words:
                print(".", end=" ")
            else:
                words.append(word.lower())
                print(word, end=" ")
        print()

main()
