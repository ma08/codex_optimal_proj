

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.lower().split()
            word = word.lower().strip(",.!?")
        for word in line:
            if word in words:
                print(".", end=" ")
            else:
                words.append(word)
                print(word, end=" ")
        print()

main()
