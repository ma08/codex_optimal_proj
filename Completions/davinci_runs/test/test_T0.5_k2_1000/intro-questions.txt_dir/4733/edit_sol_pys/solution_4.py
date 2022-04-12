#!/usr/bin/env python3

import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(num_cases):
        n = int(sys.stdin.readline().strip())
        shuffle = sys.stdin.readline().strip().lower()

        if shuffle == 'out':
            print(n//2 + 1) # integer division
        else:
            print(n-1)

if __name__ == '__main__':
    main()
