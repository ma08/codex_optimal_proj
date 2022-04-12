#!/usr/bin/env python3

import sys

def main():
    word = sys.stdin.readline().strip().lower()
    perm = sys.stdin.readline().strip().lower()

    # check if the word is a permutation of the prefix
    for i in range(len(word)):
        if word[i] not in perm[:i+1]:
            print('LOSE')
            return

    print('WIN')

main()
