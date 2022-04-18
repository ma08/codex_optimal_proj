#!/usr/bin/python

import sys

def main():
    s = sys.stdin.readline().strip()
    dictionary = {}
    for c in s:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] += 1
    count = 0
    for key in dictionary:
        if dictionary[key] % 2 != 0:
            count += 1
    print(count - 1)

if __name__ == '__main__':
    main()
