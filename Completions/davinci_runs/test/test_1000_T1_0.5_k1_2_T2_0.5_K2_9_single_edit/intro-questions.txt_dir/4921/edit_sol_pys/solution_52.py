
import sys

def main():
    words = set() # create an empty set
    for line in sys.stdin:
        for word in line.split(): # iterate over each word in the line
            if word.lower() in words:
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.add(word.lower())
        print()

main()
