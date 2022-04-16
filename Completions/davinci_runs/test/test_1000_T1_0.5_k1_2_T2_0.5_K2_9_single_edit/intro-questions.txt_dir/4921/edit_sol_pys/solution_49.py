import string

import sys

def main():
    punctuations = string.punctuation
    words = []
    for line in sys.stdin:
        line = line.split()
            word = word.strip(punctuations)
            word = word.lower()
        for word in line:
            if word in words:
                print(".", end=" ")
            else:
                words.append(word)
                print(word, end=" ")
        print()

main()
