#!/usr/bin/env python3

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().split() #strip whitespace and split into list of words
        for word in line:
            if word.lower() not in words: #lowercase the words to avoid case sensitivity when comparing
                words.append(word.lower()) #add lowercase words to the list to keep track of them
                print(word, end=' ')
            else:
                print('.', end=' ') #if the word has already been seen, print a dot
        print('')

main()
