#!/usr/bin/python3

import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(num_cases):
        n = int(sys.stdin.readline().strip())
        shuffle = sys.stdin.readline().strip()

        if shuffle == 'out':
            print(n//2 if n%2==0 else n//2+1)
        else:
            print(n-1 if n>1 else 1)

if __name__ == '__main__':
    main()
