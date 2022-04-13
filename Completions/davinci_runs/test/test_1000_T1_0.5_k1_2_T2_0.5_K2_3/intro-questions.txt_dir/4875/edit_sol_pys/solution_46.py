

import argparse
import sys

def main(args):
    for line in args.input:
        words = line.split()
        for word in words:
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                print(word + 'yay', end=' ')
            else:
                first_vowel = word.index([c for c in word if c in ['a', 'e', 'i', 'o', 'u']][0]) # get the index of the first vowel in the word
                print(word[first_vowel:] + word[:first_vowel] + 'ay', end=' ')
        print(end='\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'), nargs='?', default=sys.stdin)
    args = parser.parse_args()
    main(args)
