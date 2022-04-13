"""
# file.py

This program takes in a file and converts each word to pig latin.

"""
import sys

    """
    # pig_latin(word)

    This function takes in a word and converts it to pig latin.
    """
def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        for i in range(len(word)):
            if word[i] in 'aeiou':
                return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        line = line.strip().split(' ')
        for i in range(len(line)):
            line[i] = pig_latin(line[i])
        print(' '.join(line) + '\n')

if __name__ == '__main__':
    main()
