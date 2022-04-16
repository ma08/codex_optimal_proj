#!/usr/bin/env python3

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().split()
        for word in line:
            if word.lower().strip('.,!?()') not in words:
                words.append(word.lower().strip('.,!?()'))
                print(word, end=' ')
            else:
                print('.', end=' ')
        print('')

main()
